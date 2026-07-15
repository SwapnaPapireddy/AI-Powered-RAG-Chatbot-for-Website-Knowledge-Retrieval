"""
vector_store.py

Creates and manages FAISS vector database.
"""

import os

from langchain_community.vectorstores import FAISS


class VectorStore:

    def __init__(self, embeddings):
        self.embeddings = embeddings

    def create_vector_store(self, documents):
        """
        Create FAISS index from documents.
        """

        db = FAISS.from_documents(
            documents=documents,
            embedding=self.embeddings
        )

        return db

    def save_vector_store(
        self,
        db,
        save_path="embeddings/faiss_index"
    ):
        """
        Save FAISS index.
        """

        os.makedirs(save_path, exist_ok=True)

        db.save_local(save_path)

        print(f"Vector Store saved at {save_path}")

    def load_vector_store(
        self,
        save_path="embeddings/faiss_index"
    ):
        """
        Load FAISS index.
        """

        db = FAISS.load_local(
            folder_path=save_path,
            embeddings=self.embeddings,
            allow_dangerous_deserialization=True
        )

        return db

    def similarity_search(
        self,
        db,
        query,
        k=4
    ):
        """
        Retrieve relevant documents.
        """

        return db.similarity_search(
            query=query,
            k=k
        )

    def get_retriever(
        self,
        db,
        k=4
    ):
        """
        Return LangChain Retriever.
        """

        retriever = db.as_retriever(
            search_type="similarity",
            search_kwargs={"k": k}
        )

        return retriever