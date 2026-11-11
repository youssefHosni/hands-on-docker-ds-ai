import mlflow
import pandas as pd
from fastapi import FastAPI
from mlflow import MlflowClient
from pydantic import BaseModel

# Load the "champion" version of the iris model from MLflow (MLFLOW_TRACKING_URI comes from Compose)
version = MlflowClient().get_model_version_by_alias("iris", "champion").version
model = mlflow.sklearn.load_model("models:/iris@champion")
SPECIES = ["setosa", "versicolor", "virginica"]

app = FastAPI(title="Iris API")


class Flower(BaseModel):
    """The four measurements of an iris flower, in cm."""
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/health")
def health():
    """Health check, with the model version being served."""
    return {"status": "ok", "model_version": version}


@app.post("/predict")
def predict(flower: Flower):
    """Predict the species of one flower."""
    row = pd.DataFrame([list(flower.model_dump().values())], columns=model.feature_names_in_)
    return {"species": SPECIES[model.predict(row)[0]], "model_version": version}
