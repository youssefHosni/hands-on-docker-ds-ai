FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .
COPY data /data
RUN useradd --create-home appuser
USER appuser

CMD ["python", "server.py"]
