import numpy as np
import joblib
from sklearn.linear_model import LinearRegression

# Generate dummy data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, 'model.pkl')
print("Model saved!")
