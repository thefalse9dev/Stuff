import pandas as pd
import numpy as np
import matplotlib 
import seaborn as sns
import random
import matplotlib.pyplot as plt
from dateutil.parser import parse
from scipy import signal
from scipy.interpolate import interp1d
from scipy import stats
from statsmodels.tsa.stattools import adfuller, kpss, acf, pacf, grangercausalitytests
from statsmodels.nonparametric.smoothers_lowess import lowess
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.metrics import mean_squared_error
df=pd.read_csv('data.csv')
res = grangercausalitytests(df[['GDP','Renewable']], maxlag=7)
