#msa
Python code for calculating runs in three interval of Overs,first interval of first 6 overs and second interval of next 4 overs and third interval of next 5 overs
#######################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('source-data.csv')
dataset=dataset.fillna(0)
len(dataset)
x=np.zeros((636,3))
for i in range(1,637):
    run11=0
    run12=0
    run21=0
    for k in range(len(dataset)):
        if(dataset["match_id"][k]==i):
            if(dataset["inning"][k]==1):
                if(dataset["over"][k]>=1 and dataset["over"][k]<=6):
                    run11=run11+dataset["total_runs"][k]   
                if(dataset["over"][k]>=7 and dataset["over"][k]<=14):
                    run12=run12+dataset["total_runs"][k]
                if(dataset["over"][k]>=15 and dataset["over"][k]<=20):
                    run21=run21+dataset["total_runs"][k]   
    x[i-1][0]=run11
    x[i-1][1]=run12
    x[i-1][2]=run21
