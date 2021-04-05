import pandas as pd
import numpy as np
import matplotlib 
import seaborn as sns
import random
import matplotlib.pyplot as plt
import statistics
from scipy import stats
df=pd.read_csv('ipl.csv')
player = input("Enter the player's name: ")
for i in range(1,25):
    print("")
df = df[df['batsman']== player]
df['batsman_runs'] = df['batsman_runs'].astype(float)
df.fillna(0)
matrix=[]
dis=[]
j=1
for j in range(1,21):
    l=[]
    k=0
    for i in df.index:
        if(df.loc[i,'over']==j):
            l.append(df.loc[i,'batsman_runs'])
            if(df.loc[i,'player_dismissed']==player):
                k=k+1
    matrix.append(l)   
    dis.append(k) 
pl=pd.DataFrame(columns=['Overs','RPB','TD'])
for i in range(1,21):
    pl.loc[i,'Overs']=i
    if(len(matrix[i-1])==0):
        pl.loc[i,'RPB']=float('Nan')
    else:
        pl.loc[i,'RPB']=statistics.mean(matrix[i-1])
    pl.loc[i,'TD']=dis[i-1]
print("")
print("Player: ",player)
print("")
print(pl)
print("")
pl=pl.dropna()
correlation, p_value = stats.pearsonr(pl['RPB'],pl['TD'])
print("Correlation: ",correlation)
print("P_value: ",p_value)
print("")


