import numpy as np
import joblib
from tensorflow import keras

# Load trained model and scalers
model = keras.models.load_model("ann_model.keras")
scaler_x = joblib.load("scaler_x.joblib")
scaler_y = joblib.load("scaler_y.joblib")

# Get user input
x_input = float(input("Enter x (in radians): "))

# Scale input
x_scaled = scaler_x.transform([[x_input]])

# Predict (scaled)
y_pred_scaled = model.predict(x_scaled)

# Convert back to original scale
y_pred = scaler_y.inverse_transform(y_pred_scaled)

print(f"Predicted y value for x={x_input:.4f}: {y_pred[0][0]:.6f}")
