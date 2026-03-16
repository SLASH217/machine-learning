import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# 1. Create and train the "brain"
X_train = np.array([[1], [2], [3], [4], [5]])
y_train = np.array([5, 7, 9, 11, 13])

model = LinearRegression()
model.fit(X_train, y_train)

# 2. Save the model to your hard drive
# We must manually open a file in 'wb' (Write Binary) mode
with open("my_brain.pkl", "wb") as file:
    pickle.dump(model, file)

print("Pickle: Model trained and saved successfully!")