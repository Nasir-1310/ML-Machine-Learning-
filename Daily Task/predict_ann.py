import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # hide TF info messages

import numpy as np
from tensorflow import keras

# Load trained model
model = keras.models.load_model("ann_model.keras")

# Take x input from user
x_val = float(input("Enter x (in radians): "))

# Predict y
x_input = np.array([[x_val]])
y_pred = model.predict(x_input, verbose=0)

print(f"Predicted y value: {y_pred[0][0]}")
