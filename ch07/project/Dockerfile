FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:0.13.6 /uv /bin/uv

# The virtual environment lives in /opt/venv, outside the project folder we mount
ENV PYTHONUNBUFFERED=1 \
    UV_PYTHON_DOWNLOADS=0 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/opt/venv \
    PATH="/opt/venv/bin:$PATH"

RUN useradd --create-home appuser

# A folder for datasets, owned by appuser: a new named volume mounted here takes this owner
RUN mkdir /datasets && chown appuser /datasets

WORKDIR /project

# Only the dependencies go into the image; the code and data come in with a bind mount
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-install-project

USER appuser

EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser"]
