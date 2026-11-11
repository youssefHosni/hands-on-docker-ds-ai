# The Python version, chosen at build time (docker build --build-arg PYTHON_VERSION=...)
ARG PYTHON_VERSION=3.14
FROM python:${PYTHON_VERSION}-slim

# uv, copied from its official image
COPY --from=ghcr.io/astral-sh/uv:0.13.6 /uv /bin/uv

# Print logs at once; let uv use the image's Python; put the virtual environment on the PATH
ENV PYTHONUNBUFFERED=1 \
    UV_PYTHON_DOWNLOADS=0 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PATH="/app/.venv/bin:$PATH"

# A regular user to run the application
RUN useradd --create-home appuser

WORKDIR /app

# Install the locked dependencies first; the cache mount keeps uv's downloads between builds
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-install-project --no-dev

# Copy the code and train the model
COPY . .
RUN python train.py

# From here on, run as the regular user, not root
USER appuser

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
