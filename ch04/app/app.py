from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import logging

# Initialize FastAPI App
app = FastAPI(title="ML Prediction API")

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load Model
MODEL_PATH = "model.pkl"
try:
    model = joblib.load(MODEL_PATH)
    logging.info(f"Model loaded successfully from {MODEL_PATH}")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    model = None


class PredictRequest(BaseModel):
    """The request body: the numbers to predict for."""
    input: list[float]


@app.get("/")
def home():
    """Root endpoint - API Welcome Message."""
    return {
        "message": "Welcome to the ML Prediction API!",
        "endpoints": {
            "Predict": "/predict (POST)",
            "Health": "/health",
            "Docs": "/docs"
        }
    }


@app.get("/health")
def health():
    """Health check endpoint, used by Docker's HEALTHCHECK."""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictRequest):
    """Endpoint to make predictions using the trained model."""
    if model is None:
        logging.error("Prediction request failed: Model not loaded.")
        raise HTTPException(status_code=500, detail="Model not loaded")
    if not request.input:
        logging.warning("Prediction request failed: Missing 'input' data.")
        raise HTTPException(status_code=400, detail="Missing 'input' data")
    # Convert input to NumPy array and make prediction
    prediction = model.predict(np.array(request.input).reshape(-1, 1))
    logging.info(f"Prediction successful: {prediction.tolist()}")
    return {"prediction": prediction.tolist()}
