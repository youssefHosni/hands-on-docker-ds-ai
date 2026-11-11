FROM python:3.14-slim

# Where to get PyTorch: PyPI by default (on Linux, it brings its own CUDA libraries),
# or one of PyTorch's own indexes, e.g. https://download.pytorch.org/whl/cpu
ARG TORCH_INDEX=https://pypi.org/simple
RUN pip install --no-cache-dir --index-url ${TORCH_INDEX} torch==2.15.0

WORKDIR /app
COPY check_gpu.py .
CMD ["python", "check_gpu.py"]
