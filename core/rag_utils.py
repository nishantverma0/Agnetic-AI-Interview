import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

class RAGRetriever:
    def __init__(self, docs):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)
        self.docs = docs
        embeddings = self.model.encode(docs)
        self.index.add(np.array(embeddings))

    def query(self, q, top_k=2):
        q_emb = self.model.encode([q])
        distances, indices = self.index.search(np.array(q_emb), top_k)
        return [self.docs[i] for i in indices[0]]
