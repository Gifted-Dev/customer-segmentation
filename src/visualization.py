import matplotlib.pyplot as plt

def plot_clusters(df, x_col, y_col, cluster_col):
    """Visualize clusters on a 2D scatter plot."""
    plt.scatter(df[x_col], df[y_col], c=df[cluster_col], cmap='viridis')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title('Customer Segments')
    plt.show()
    
    
# def plot_clusters_with_centroids(df, x_col, y_col, cluster_col, centroids):
#     """Visualize clusters on a 2D scatter plot with centroids."""
#     plt.figure(figsize=(8, 6))

#     # Plot the clusters
#     plt.scatter(df[x_col], df[y_col], c=df[cluster_col], cmap='viridis', label='Clusters', alpha=0.6)

#     # Plot the centroids
#     x_idx = centroid_features.index(x_col)
    
#     y_idx = centroid_features.index(y_col)
#     plt.scatter(centroids[:, x_idx], centroids[:, y_idx], c='red', s=200, marker='X', label='Centroids')
    

#     plt.xlabel(x_col)
#     plt.ylabel(y_col)
#     plt.title('Customer Segments with Centroids')
#     plt.legend()
#     plt.show()
   

# def evaluate_klusters():
#     ks = range(1, 6)
#     inertias = []

#     for k in ks:
#         # Create a KMeans instance with k clusters: model
#         model = KMeans(n_clusters=k)
        
#         # Fit model to samples
#         model.fit(samples)
        
#         # Append the inertia to the list of inertias
#         inertias.append(model.inertia_)
        
#     # Plot ks vs inertias
#     plt.plot(ks, inertias, '-o')
#     plt.xlabel('number of clusters, k')
#     plt.ylabel('inertia')
#     plt.xticks(ks)
#     plt.show()