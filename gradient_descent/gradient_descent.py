import numpy as np
import pandas as pd
import math
def gradient_descent(x,y, learning_rate):
  # Starting the slope and intercept at zero
  m_curr = b_curr = 0
  # How many baby steps to do?
  iterations = 1000000

  # learning_rate = 0.08

  previous_cost = 0
  # tolerance = 1e-6

  n = len(x)
  for _i in range(iterations):
    y_predicted = m_curr * x + b_curr
    cost = (1/n) * sum ((y - y_predicted)**2)
    # if abs(previous_cost - cost) < tolerance:
    if math.isclose(previous_cost, cost, rel_tol=1e-20):
      print(f"Algorithm converged! Stopping early at iteration {_i}")
      print(f"Final Cost: {cost}, m: {m_curr}, b: {b_curr}")
      break
    md = -(2/n) * sum(x * (y -y_predicted))
    bd = -(2/n) * sum(y - y_predicted)
    m_curr = m_curr - learning_rate * md
    b_curr = b_curr - learning_rate * bd
    previous_cost = cost
    # print(m_curr, b_curr, _i ,cost)

# with open ("excercise/test_scores.csv", 'r') as file:
#   print(file.read())
df = pd.read_csv("excercise/test_scores.csv")
# print(df)
# print(df.math)
# print(df.cs)

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

p = np.array(df.math)
r = np.array(df.cs)
# print(p)
# print(r)
# gradient_descent(x,y, 0.08)

gradient_descent(p,r,0.0001)