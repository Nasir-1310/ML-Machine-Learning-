import pandas as pd
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

# Step 1: Read data from Excel
data = pd.read_excel("data.xlsx")
print("Available columns:", data.columns)

# Use correct column names based on your Excel
x = data["x"].values
y = data["y"].values

# Reshape inputs
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)

# Step 2: Get user input for model structure
num_hidden_layers = int(input("Enter number of hidden layers: "))
neurons_per_layer = int(input("Enter number of neurons per hidden layer: "))

# Step 3: Build the ANN model dynamically
model = keras.Sequential()
model.add(layers.Input(shape=(1,)))  # 1 input feature

for i in range(num_hidden_layers):
    model.add(layers.Dense(neurons_per_layer, activation='relu'))
    print(f"✅ Added hidden layer {i+1} with {neurons_per_layer} neurons.")

model.add(layers.Dense(1))  # Output layer

# Step 4: Compile model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
print("\nModel compiled successfully!")

# Step 5: Train model
print("\n🚀 Training started...")
model.fit(x, y, epochs=1000, verbose=1)
print("\n✅ Training completed successfully!")

# Step 6: Save model
model.save("ann_model.keras")
print("✅ Model saved as 'ann_model.keras'")
