import pickle

# 1. Load the model back into memory
# We must manually open the file in 'rb' (Read Binary) mode
with open("my_brain.pkl", "rb") as file:
    loaded_model = pickle.load(file)

# 2. Ask the loaded brain to make a prediction
prediction = loaded_model.predict([[6]])

print(f"Pickle: The predicted value for 6 is {prediction[0]}")