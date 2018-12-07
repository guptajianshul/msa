import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('final cricket data1.csv')
x=np.zeros((636,1))
for i in range(1,637):
    run11=0
    run12=0
    for k in range(len(dataset)):
        if(dataset["match_id"][k]==i):
            if(dataset["inning"][k]==1):
                run11=run11+dataset["total_runs"][k]
        x[i-1][0]=run11
    
