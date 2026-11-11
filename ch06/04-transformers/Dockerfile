FROM pytorch/pytorch:2.15.0-cuda13.4-cudnn9-runtime
# This image's Python belongs to Ubuntu, which blocks pip unless we say so (PEP 668)
RUN pip install --no-cache-dir --break-system-packages transformers==5.22.1
WORKDIR /app
COPY main.py .
CMD ["python", "main.py"]
