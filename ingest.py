# ingest.py

import os
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.embeddings import Embeddings
from typing import List

DATA_PATH = "sample_data.txt"
VECTOR_PATH = "vectorstore"

# Simple embedding class to avoid heavy dependencies
class SimpleEmbeddings(Embeddings):
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        import hashlib
        embeddings = []
        for text in texts:
            # Create a simple deterministic embedding from text hash
            hash_obj = hashlib.md5(text.encode())
            hash_val = int(hash_obj.hexdigest(), 16)
            # Generate a fixed-size embedding
            embedding = []
            for i in range(384):
                embedding.append(float((hash_val >> i) & 1) * 2 - 1)
            embeddings.append(embedding)
        return embeddings
    
    def embed_query(self, text: str) -> List[float]:
        return self.embed_documents([text])[0]

def ingest_documents():
    # Read text file
    with open(DATA_PATH, 'r') as f:
        content = f.read()
    
    # Create document
    documents = [Document(page_content=content, metadata={"source": DATA_PATH})]

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    docs = text_splitter.split_documents(documents)

    embeddings = SimpleEmbeddings()

    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(VECTOR_PATH)

    print("✅ Documents ingested successfully!")

if __name__ == "__main__":
    ingest_documents()
