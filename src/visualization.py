import matplotlib.pyplot as plt

def plot_clusters(df, x_col, y_col, cluster_col):
    """Visualize clusters on a 2D scatter plot."""
    plt.scatter(df[x_col], df[y_col], c=df[cluster_col], cmap='viridis')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title('Customer Segments')
    plt.show()
