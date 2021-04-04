import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
data = pd.read_csv("data.csv")
x=np.array(data['Total Energy']).reshape((-1,1))
y=np.array(data['GDP'])
model=LinearRegression().fit(x,y)
print("R_sq: ",model.score(x,y))
print("A: ",model.intercept_)
print("B: ",model.coef_)