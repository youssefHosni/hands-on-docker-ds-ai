FROM nvidia/cuda:13.4.3-runtime-ubuntu24.04
# The CUDA images have no Python: install it, with a virtual environment for your packages (PEP 668)
RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 python3-venv \
    && rm -rf /var/lib/apt/lists/*
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /app
COPY main.py .
CMD ["python", "main.py"]
