import joblib

# 1. Load the model back into memory
# Syntax: joblib.load("filename.joblib")
loaded_model = joblib.load("my_brain.joblib")

# 2. Ask the loaded brain to make a prediction
# We are asking: "What is the output if X is 6?"
prediction = loaded_model.predict([[6]])

print(f"Joblib: The predicted value for 6 is {prediction[0]}")