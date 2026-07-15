"""
retriever.py

Creates the retriever from the FAISS vector store.
"""


class Retriever:

    def __init__(self, vector_db, k=4):
        self.vector_db = vector_db
        self.k = k

    def get_retriever(self):
        """
        Returns LangChain retriever.
        """

        return self.vector_db.as_retriever(
            search_type="similarity",
            search_kwargs={
                "k": self.k
            }
        )

    def retrieve_documents(self, query):
        """
        Retrieve relevant documents.
        """

        docs = self.vector_db.similarity_search(
            query=query,
            k=self.k
        )

        return docs