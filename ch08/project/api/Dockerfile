FROM python:3.14-slim
RUN pip install --no-cache-dir fastapi==0.162.0 uvicorn==0.54.0 mlflow-skinny==3.17.2 scikit-learn==1.9.1 pandas==3.1.0 skops==0.16.0
RUN useradd --create-home appuser
USER appuser
WORKDIR /app
COPY app.py .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
