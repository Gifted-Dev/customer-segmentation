import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file):
    """Load dataset from a CSV file"""
    return pd.read_csv(file)

def clean_data(df):
    """Clean the dataset i.e. handle missing values"""
    df.dropna(inplace=True)
    return df

def scale_features(df, features):
    """Normalize features using StandardScaler"""
    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features])
    return df

