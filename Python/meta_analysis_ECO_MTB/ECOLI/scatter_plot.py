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
regression_line = sns.regplot(df['90_min_after_cold_stress'], df['90_min_after_oxy_stress'], color = "blue", ci = None)
r_squared = r2_score(df['90_min_after_cold_stress'], df['90_min_after_oxy_stress'])
new_plot = plt.scatter(df['90_min_after_cold_stress'], df['90_min_after_oxy_stress'], s = 60, alpha = 0.75, c = "purple", edgecolor = "k")
plt.xlabel("Ninety minutes after cold stress")
plt.ylabel("Ninety minutes after oxydative stress")
plt.show()
