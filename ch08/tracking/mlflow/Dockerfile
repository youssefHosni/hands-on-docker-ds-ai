FROM ghcr.io/mlflow/mlflow:v3.17.2
# The MLflow image has no PostgreSQL driver: add one (psycopg 3, the one SQLAlchemy 2.1 uses)
RUN pip install --no-cache-dir "psycopg[binary]==3.3.6"
