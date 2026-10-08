import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 1: Load dataset
data = pd.read_csv("data/air_quality.csv")

# Step 2: Select required columns
data = data[['City','PM2.5','PM10','NO2','CO','SO2','AQI']]

# Step 3: Handle missing values
data = data.dropna()

print("After cleaning:", data.shape)

# Step 4: Select features
X = data[['PM2.5','PM10','NO2','CO','SO2']]

# Step 5: Normalize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 6: Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(X_scaled)

# Step 7: Label clusters based on AQI
cluster_avg = data.groupby('Cluster')['AQI'].mean().sort_values()

labels = {
    cluster_avg.index[0]: "Low Pollution",
    cluster_avg.index[1]: "Moderate Pollution",
    cluster_avg.index[2]: "High Pollution"
}

data['Category'] = data['Cluster'].map(labels)

# Step 8: Save output
data.to_csv("results/output.csv", index=False)

print(data[['City','AQI','Category']].head())
print("Clustering Completed!")

# ===========================
#  VISUALIZATION (FINAL)
# ===========================

plt.figure(figsize=(10,6))

# Colors for clusters
colors = ['green', 'orange', 'red']

for cluster in data['Cluster'].unique():
    cluster_data = data[data['Cluster'] == cluster]
    
    plt.scatter(
        cluster_data['PM2.5'],
        cluster_data['PM10'],
        color=colors[cluster],
        label=labels[cluster],
        alpha=0.6
    )

# Plot centroids
centroids = kmeans.cluster_centers_

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    s=300,
    c='black',
    marker='X',
    label='Centroids'
)

plt.xlabel("PM2.5")
plt.ylabel("PM10")
plt.title("K-Means Pollution Clusters")
plt.legend()
plt.grid()

plt.show()