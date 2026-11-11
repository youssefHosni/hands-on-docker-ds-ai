# Airflow with its official Compose file

The book runs Airflow's own `docker-compose.yaml`; it isn't copied here. In an empty folder:

```bash
curl -LfO https://airflow.apache.org/docs/apache-airflow/3.3.2/docker-compose.yaml
mkdir -p dags logs plugins config && echo "AIRFLOW_UID=$(id -u)" > .env
docker compose up airflow-init
docker compose up -d
```

Open `http://localhost:8080` (user `airflow`, password `airflow`). Stop and delete everything with
`docker compose down -v`.
