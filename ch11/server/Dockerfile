FROM python:3.14-slim AS base

ENV PYTHONUNBUFFERED=1 \
    HF_HOME=/models

WORKDIR /app

# The CPU-only build of PyTorch, then the server's packages
COPY requirements.txt .
RUN pip install --no-cache-dir torch==2.15.0 --index-url https://download.pytorch.org/whl/cpu \
 && pip install --no-cache-dir -r requirements.txt

# A regular user, who owns the folder where models are stored
RUN useradd --create-home appuser \
 && mkdir /models && chown appuser /models
USER appuser

# The model and the exact version of it that we tested
ENV MODEL_ID=distilbert/distilbert-base-uncased-finetuned-sst-2-english \
    MODEL_REVISION=714eb0fa89d2f80546fda750413ed43d93601a13


# Downloads the model; only the baked stage uses it
FROM base AS model
COPY download.py .
RUN python download.py


# The model server, which downloads the model when it starts
FROM base AS server
COPY app.py .
EXPOSE 8000
HEALTHCHECK --interval=10s --timeout=3s --start-period=60s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]


# The same server, with the model inside the image
FROM server AS baked
COPY --from=model --chown=appuser /models /models
ENV HF_HUB_OFFLINE=1
