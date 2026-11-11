FROM python:3.14-slim
RUN pip install --no-cache-dir mlflow-skinny==3.17.2 scikit-learn==1.9.1 pandas==3.1.0 skops==0.16.0
RUN useradd --create-home appuser
USER appuser
WORKDIR /app
COPY train.py .
CMD ["python", "train.py"]
