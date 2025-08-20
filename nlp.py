import numpy as np
class TextEmbedder:
    """Dummy text embedder that converts text into simple embeddings.
       Replace with a real model later (e.g., SentenceTransformer).
    """
    def transform_rows(self, df):
        n_rows = len(df)
        return np.random.rand(n_rows, 100)
