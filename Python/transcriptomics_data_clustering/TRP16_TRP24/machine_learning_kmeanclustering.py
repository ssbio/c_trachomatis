#IMPORT MODULES
from sklearn.cluster import KMeans
import numpy as NP
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt

#LOAD FILES
df = pd.read_csv("chlamydia_KMC.csv")
df.head()
#new_plot = plt.scatter(df['BPD24'], df['TRP24'])
#plt.show()

#DETERMINE NUMBER OF CLUSTERS USING ELBOW METHODS
#COMMENT OUT FROM "PERFORM K MEAN CLUSTERING" TO "PLOTTING RESULTS" WHILE RUNNING CODES FROM LINE 15 TO LINE 25
# k_rng = range(1,10)
# sse = []
# for k in k_rng:
#     km = KMeans(n_clusters = k)
#     km.fit(df[['UTD24','TRP24']])
#     sse.append(km.inertia_)
#     
# plt.xlabel('K')
# plt.ylabel('Sum of squared error')
# plt.plot(k_rng,sse)
# plt.show()

#PERFORM K MEAN CLUSTERING
km = KMeans(n_clusters = 4)
y_predicted = km.fit_predict(df[['TRP16','TRP24']])
df['cluster'] = y_predicted
df.head()

#PLOTTING RESULTS
df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]
df4 = df[df.cluster == 3]
plt.scatter(df2['TRP16'], df2['TRP24'], color = 'blue', s = 60, alpha = 0.75, edgecolor = "k")
plt.scatter(df1['TRP16'], df1['TRP24'], color = 'green', s = 60, alpha = 0.75, edgecolor = "k")
plt.scatter(df4['TRP16'], df4['TRP24'], color = 'orange', s = 60, alpha = 0.75, edgecolor = "k")
plt.scatter(df3['TRP16'], df3['TRP24'], color = 'red', s = 60, alpha = 0.75, edgecolor = "k")

plt.title('16 Hours of Tryptophan Starvation vs 24 Hours of Tryptophan Starvation')
plt.xlabel('TRP16')
plt.ylabel('TRP24')
plt.legend()
plt.show()

#WRITE THE ARRAY IN AN EXCEL FILE
output = pd.DataFrame(df).T
output.to_excel(excel_writer = "C:/Users/niazc/OneDrive/Desktop/chlamydia_trachomatis/Result/chlamydia_only/Hypothesis1/TRP16_TRP24/TRP16_TRP24.xlsx")

#PREDICTING CLUSTERS WHEN NEW DATA IS AVAILABLE
# centroids = km.cluster_centers_
# new_data = NP.array([0.2,0.6])
# diff = centroids - new_data
# dist = NP.sqrt(NP.sum(diff**2, axis=-1))
# closest_centroid = centroids[NP.argmin(dist),]
# print(closest_centroid)