# ---- Stage 1: install the packages the API needs ----
FROM python:3.14-slim AS build
COPY --from=ghcr.io/astral-sh/uv:0.13.6 /uv /bin/uv
ENV UV_PYTHON_DOWNLOADS=0 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PATH="/app/.venv/bin:$PATH"
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-install-project --no-dev

# ---- Stage 2: add the training packages and train the model ----
FROM build AS train
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-install-project --no-dev --group train
COPY train.py .
COPY data/ data/
RUN python train.py

# ---- Stage 3: the image we ship ----
FROM python:3.14-slim
ENV PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"
# The API doesn't need pip: remove it, with the packages it carries inside
RUN pip uninstall --yes --root-user-action=ignore pip && useradd --create-home appuser
WORKDIR /app
COPY --from=build /app/.venv /app/.venv
COPY --from=train /app/model.pkl .
COPY app.py .
USER appuser
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
