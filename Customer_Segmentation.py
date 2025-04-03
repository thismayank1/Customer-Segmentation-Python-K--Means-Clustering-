import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the dataset
df = pd.read_csv("E-commerce.csv")  # Ensure the file is in the same directory

# Select relevant numerical features for clustering
features = df[['Age', 'Annual Income', 'Time on Site']]

# Standardize the features for better clustering performance
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Determine the optimal number of clusters using the Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(scaled_features)
    wcss.append(kmeans.inertia_)

# Plot the Elbow Method graph
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='o', linestyle='-')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.title('Elbow Method for Optimal Clusters')
plt.show()

# Fit K-Means with the optimal number of clusters (assumed 3 based on the elbow graph)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(scaled_features)

# Perform PCA for better visualization
pca = PCA(n_components=2)
pca_features = pca.fit_transform(scaled_features)
df['PCA1'] = pca_features[:, 0]
df['PCA2'] = pca_features[:, 1]

# Interactive Plotly Visualization
fig = px.scatter(df, x='PCA1', y='PCA2', color=df['Cluster'].astype(str), 
                  title='Customer Segmentation using K-Means (PCA Reduced)',
                  labels={'Cluster': 'Segment'},
                  hover_data=['Age', 'Annual Income', 'Time on Site'])
fig.show()

# Save the clustered data
df.to_csv("customer_segments.csv", index=False)
print("Customer segmentation completed. Results saved in 'customer_segments.csv'.")
