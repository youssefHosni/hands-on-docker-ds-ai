FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py train.py .
RUN python train.py

RUN useradd --uid 1000 --create-home appuser
USER 1000

# The platform can choose the port. exec makes uvicorn PID 1, so it gets the stop signal.
ENV PORT=8000
EXPOSE 8000
CMD ["sh", "-c", "exec uvicorn app:app --host 0.0.0.0 --port $PORT"]
