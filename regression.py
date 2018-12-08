import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset1=pd.read_excel('total runs of both innings.xlsx')

dataset2=pd.read_excel('I1DS.xlsx')

x1=dataset2.iloc[0:637,6].values
y1=dataset2.iloc[0:637,0].values
y2=dataset2.iloc[0:637,1].values

plt.scatter(y1,x1,color='red')
plt.title('Fall of wicket between 11-15 overs vs avg run-rate')
plt.xlabel('Fall of wicket between 11-15 overs')
plt.ylabel('avg run-rate')
plt.show()


plt.scatter(y2,x1,color='red')
plt.title('Fall of wicket between 16-20 overs vs avg run-rate')
plt.xlabel('Fall of wicket between 16-20 overs')
plt.ylabel('avg run-rate')
plt.show()


import pandas as pd
import statsmodels.formula.api as sm
df = pd.DataFrame({"A": x1, "B": y1, "C": y2})
result = sm.ols(formula="A ~ B + C", data=df).fit()
print(result.params)

print (result.summary())
