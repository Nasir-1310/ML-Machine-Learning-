import pandas as pd
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.preprocessing import MinMaxScaler
import joblib

# Step 0: User input for model configuration
# Define model architecture
#  num_hidden_layers = 3 
# neurons_per_layer = 64
num_hidden_layers = int(input("Enter the number of hidden layers: "))
neurons_per_layer = int(input("Enter the number of neurons per hidden layer: "))

# Step 1: Read data
data = pd.read_excel("data.xlsx")
x = data["x"].values.reshape(-1, 1)
y = data["y"].values.reshape(-1, 1)

# Step 2: Normalize data
scaler_x = MinMaxScaler()
scaler_y = MinMaxScaler()

x_scaled = scaler_x.fit_transform(x)
y_scaled = scaler_y.fit_transform(y)

# Save scalers for later use
joblib.dump(scaler_x, "scaler_x.joblib")
joblib.dump(scaler_y, "scaler_y.joblib")

# Step 3: Define model architecture
model = keras.Sequential()
model.add(layers.Input(shape=(1,)))

for i in range(num_hidden_layers):
    model.add(layers.Dense(neurons_per_layer, activation='tanh'))

model.add(layers.Dense(1))  # Output layer

# Step 4: Compile and train model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
print("\n🚀 Training started...\n")
model.fit(x_scaled, y_scaled, epochs=2000, verbose=1)
print("\n✅ Training completed successfully!")

# Step 5: Save model
model.save("ann_model.keras")
print("✅ Model and scalers saved successfully!")
