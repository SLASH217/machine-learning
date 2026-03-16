import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# 1. Create and train the "brain"
X_train = np.array([[1], [2], [3], [4], [5]])
y_train = np.array([5, 7, 9, 11, 13])

model = LinearRegression()
model.fit(X_train, y_train)

# 2. Save the model to your hard drive
# Syntax: joblib.dump(your_model_object, "filename.joblib")
joblib.dump(model, "my_brain.joblib")

print("Joblib: Model trained and saved successfully!")