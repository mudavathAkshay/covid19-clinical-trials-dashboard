import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def basic_tabular_features(df: pd.DataFrame):
    """Extract simple numeric features and return with a preprocessor."""
    # Select only numeric columns
    X_tab = df.select_dtypes(include=[np.number]).copy()
    preprocessor = StandardScaler()
    return X_tab, preprocessor

def combine_tabular_and_text(tabular_matrix, text_embeddings):
    """Concatenate numeric features with text embeddings."""
    return np.hstack([tabular_matrix, text_embeddings])
