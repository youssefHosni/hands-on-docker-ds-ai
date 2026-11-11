FROM python:3.14-slim
RUN pip install --no-cache-dir openai==3.42.1
RUN useradd --create-home appuser
USER appuser
WORKDIR /app
COPY chat.py .
ENTRYPOINT ["python", "chat.py"]
