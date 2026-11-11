# Chapter 3's Dockerfile, running as a regular user and with a health check
FROM python:3.14-slim
# A regular user to run the application
RUN useradd --create-home appuser
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python train.py
# From here on, run as the regular user, not root
USER appuser
EXPOSE 8000
# Chapter 3's app has no /health route, so the check asks for the welcome page
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/')"
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
