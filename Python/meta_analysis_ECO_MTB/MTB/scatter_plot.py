#IMPORT MODULES
from sklearn.cluster import KMeans
import numpy as NP
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score
from matplotlib import pyplot as plt
import seaborn as sns

#LOAD FILES
df = pd.read_csv("chlamydia_KMC.csv")
df.head()
regression_line = sns.regplot(df['ZLM'], df['ZRM'], color = "blue", ci = None)
r_squared = r2_score(df['ZLM'], df['ZRM'])
new_plot = plt.scatter(df['ZLM'], df['ZRM'], s = 60, alpha = 0.75, c = "red", edgecolor = "k")
plt.xlabel("SF20 24 Hours")
plt.ylabel("ZLM")
plt.show()
