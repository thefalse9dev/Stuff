import pandas as pd
import numpy as np
import matplotlib 
import seaborn as sns
import random
import matplotlib.pyplot as plt
import statistics
from scipy import stats
player='KL Rahul'
df1= pd.read_csv('deliveries.csv')
vk = df1[df1['batsman']== player]
vk['batsman_runs'] = vk['batsman_runs'].astype(float)
k=0
j=1
o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15,o16,o17,o18,o19,o20=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
dis=[]
vk.fillna(0)
df = pd.DataFrame(columns =['Over', 'RPB','TD'])
for i in vk.index:
    if(vk.loc[i,'over']==1):
        o1.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==2):
        o2.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==3):
        o3.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==4):
        o4.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==5):
        o5.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==6):
        o6.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==7):
        o7.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==8):
        o8.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==9):
        o9.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==10):
        o10.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==11):
        o11.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==12):
        o12.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==13):
        o13.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==14):
        o14.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==15):
        o15.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==16):
        o16.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==17):
        o17.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==18):
        o18.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==19):
        o19.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'over']==20):
        o20.append(vk.loc[i,'batsman_runs'])
    if(vk.loc[i,'player_dismissed'] == player):
        dis.append(vk.loc[i,'over'])
for i in range(1,21):
    df.loc[i,'Over']=i
    df.loc[i,'TD']=dis.count(i)
for i in df.index:
    if(df.loc[i,'Over']==1):
        df.loc[i,'RPB']=statistics.mean(o1)
    if(df.loc[i,'Over']==2):
        df.loc[i,'RPB']=statistics.mean(o2)
    if(df.loc[i,'Over']==3):
        df.loc[i,'RPB']=statistics.mean(o3)
    if(df.loc[i,'Over']==4):
        df.loc[i,'RPB']=statistics.mean(o4)
    if(df.loc[i,'Over']==5):
        df.loc[i,'RPB']=statistics.mean(o5)
    if(df.loc[i,'Over']==6):
        df.loc[i,'RPB']=statistics.mean(o6)
    if(df.loc[i,'Over']==7):
        df.loc[i,'RPB']=statistics.mean(o7)
    if(df.loc[i,'Over']==8):
        df.loc[i,'RPB']=statistics.mean(o8)
    if(df.loc[i,'Over']==9):
        df.loc[i,'RPB']=statistics.mean(o9)
    if(df.loc[i,'Over']==10):
        df.loc[i,'RPB']=statistics.mean(o10)
    if(df.loc[i,'Over']==11):
        df.loc[i,'RPB']=statistics.mean(o11)
    if(df.loc[i,'Over']==12):
        df.loc[i,'RPB']=statistics.mean(o12)
    if(df.loc[i,'Over']==13):
        df.loc[i,'RPB']=statistics.mean(o13)
    if(df.loc[i,'Over']==14):
        df.loc[i,'RPB']=statistics.mean(o14)
    if(df.loc[i,'Over']==15):
        df.loc[i,'RPB']=statistics.mean(o15)
    if(df.loc[i,'Over']==16):
        df.loc[i,'RPB']=statistics.mean(o16)
    if(df.loc[i,'Over']==17):
        df.loc[i,'RPB']=statistics.mean(o17)
    if(df.loc[i,'Over']==18):
        df.loc[i,'RPB']=statistics.mean(o18)
    if(df.loc[i,'Over']==19):
        df.loc[i,'RPB']=statistics.mean(o19)
    if(df.loc[i,'Over']==20):
        df.loc[i,'RPB']=statistics.mean(o20)
RPB=df['RPB'].tolist()
TD=df['TD'].tolist()
print("Batsman: ",player)

print("")
print(df)
print("")
correlation, p_value = stats.pearsonr(RPB,TD)
print("Correlation: ",correlation)
print("P_value: ",p_value)
print("")
    