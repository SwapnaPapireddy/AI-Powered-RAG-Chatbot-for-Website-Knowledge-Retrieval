"""
splitter.py

Splits documents into smaller chunks.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentSplitter:
    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split_documents(self, documents):
        """
        Split LangChain Documents.

        Args:
            documents: List[Document]

        Returns:
            List[Document]
        """
        return self.splitter.split_documents(documents)