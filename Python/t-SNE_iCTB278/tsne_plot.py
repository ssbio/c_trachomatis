import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv('sample_results.csv', dtype=str)

# Convert all columns except the first one to float
df.iloc[:, 1:] = df.iloc[:, 1:].astype(float)

# Drop any rows with missing values
df.dropna(inplace=True)

# Run t-SNE on the data
tsne = TSNE(n_components=2, perplexity=5, n_iter=5000, random_state=42)
tsne_results = tsne.fit_transform(df.iloc[:, 1:])

# Use K-means clustering to obtain clusters
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(tsne_results)

# Save t-SNE values and cluster assignments for each reaction to a text file
with open('tsne_results_clusters.txt', 'w') as f:
    for i, row in df.iterrows():
        reaction_id = row[0]
        tsne_x = tsne_results[i][0]
        tsne_y = tsne_results[i][1]
        cluster = clusters[i]
        f.write(f"{reaction_id}\t{tsne_x}\t{tsne_y}\t{cluster}\n")

# Plot the t-SNE results with clusters
plt.scatter(tsne_results[:, 0], tsne_results[:, 1], c=clusters)
plt.title('t-SNE Plot with Clusters')
plt.xlabel('t-SNE Dimension 1')
plt.ylabel('t-SNE Dimension 2')
plt.show()