FROM python:3.14-slim
RUN useradd --create-home appuser
USER appuser
WORKDIR /app
COPY load.py .
ENTRYPOINT ["python", "load.py"]
