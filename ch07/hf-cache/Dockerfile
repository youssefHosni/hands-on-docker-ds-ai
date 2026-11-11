FROM python:3.14-slim

# The CPU-only build of PyTorch (no CUDA libraries), then Transformers
RUN pip install --no-cache-dir torch==2.15.0 --index-url https://download.pytorch.org/whl/cpu \
 && pip install --no-cache-dir transformers==5.22.1

RUN useradd --create-home appuser
USER appuser

# Hugging Face's cache folder, created by appuser so a new volume mounted here belongs to appuser
RUN mkdir -p /home/appuser/.cache/huggingface

WORKDIR /app
COPY main.py .
CMD ["python", "main.py"]
