import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats
data = pd.read_csv("data.csv")
print("")
x=data[['LRenewable','LGCFC','LLF']]
y=data['LGDP']
X2 = sm.add_constant(x)
est = sm.OLS(y, X2)
est2 = est.fit()
print("LGDP = A + B1*LRenewable + B2*LGCFC + B3*LLF")
print()
print(est2.summary())