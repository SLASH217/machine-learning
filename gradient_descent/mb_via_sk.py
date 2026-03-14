from sklearn import linear_model
import pandas as pd


df = pd.read_csv("excercise/test_scores.csv")

reg = linear_model.LinearRegression()

reg.fit(df[["math"]], df.cs)

print(reg.coef_)
print(reg.intercept_)

# Both the gradient descent method and sk learn method yielded the same values for coef and intercept
# Seems like gradient descent had more accurate value. They are till 3 decimal points.

