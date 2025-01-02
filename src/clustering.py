from sklearn.cluster import KMeans

def kmeans_clustering(df, n_clusters, features):
    """Apply K-Means clustering"""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Cluster'] = kmeans.fit_predict(df[features])
    return df, kmeans