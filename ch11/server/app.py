import json
import logging
import os
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Response
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest
from pydantic import BaseModel, Field
from transformers import pipeline

# Which model to serve, and the exact version of it (a commit on the Hugging Face Hub)
MODEL_ID = os.environ["MODEL_ID"]
MODEL_REVISION = os.environ["MODEL_REVISION"]

# One JSON object per log line, easy to search and to send to a log tool
logging.basicConfig(format="%(message)s")
log = logging.getLogger("server")
log.setLevel(logging.INFO)

# Metrics for Prometheus, served on /metrics
PREDICTIONS = Counter("predictions_total", "Texts classified, by label", ["label"])
LATENCY = Histogram("predict_seconds", "Time the model takes per request")

model = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the model once, before the server accepts its first request
    start = time.perf_counter()
    model["sentiment"] = pipeline(
        "sentiment-analysis", model=MODEL_ID, revision=MODEL_REVISION
    )
    seconds = round(time.perf_counter() - start, 2)
    log.info(json.dumps({"event": "model_loaded", "model": MODEL_ID, "seconds": seconds}))
    yield


app = FastAPI(lifespan=lifespan)


class Reviews(BaseModel):
    texts: list[str] = Field(min_length=1, max_length=32)


@app.get("/health")
def health():
    return {"status": "ok", "model": MODEL_ID, "revision": MODEL_REVISION[:7]}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.post("/predict")
def predict(reviews: Reviews):
    start = time.perf_counter()
    results = model["sentiment"](reviews.texts, truncation=True)
    seconds = time.perf_counter() - start

    LATENCY.observe(seconds)
    for result in results:
        PREDICTIONS.labels(result["label"]).inc()
    log.info(json.dumps({"event": "predict", "texts": len(results), "seconds": round(seconds, 3)}))

    return [{"label": r["label"], "score": round(r["score"], 3)} for r in results]
