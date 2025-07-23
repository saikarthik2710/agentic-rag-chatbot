# embeddings/vector_store.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)
        self.chunks = []

    def add_document(self, text):
        chunks = text.split("\n\n")  # Naive chunking
        embeddings = self.model.encode(chunks)
        self.index.add(np.array(embeddings).astype("float32"))
        self.chunks.extend(chunks)

    def query(self, query_text, top_k=3):
        q_embedding = self.model.encode([query_text])
        D, I = self.index.search(np.array(q_embedding).astype("float32"), top_k)
        return [self.chunks[i] for i in I[0]]
