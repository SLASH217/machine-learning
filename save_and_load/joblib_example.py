import joblib
import numpy as np

# 1. The data we want to save (a massive NumPy array)
# Imagine this is the internal weight matrix of a trained model
massive_weights_array = np.random.rand(1000, 1000)

# 2. Saving (Serialization)
joblib.dump(massive_weights_array, "model_weights.joblib")
print("Joblib: Array saved successfully!")

# 3. Loading (Deserialization)
loaded_weights = joblib.load("model_weights.joblib")

print(f"Joblib: Loaded array with shape {loaded_weights.shape}")
