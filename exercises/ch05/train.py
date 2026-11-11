import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

# Load the training data
data = pd.read_csv("data/train.csv")

# Train model
model = LinearRegression()
model.fit(data[["x"]].to_numpy(), data["y"].to_numpy())

# Save model
joblib.dump(model, "model.pkl")
print("Model saved!")
