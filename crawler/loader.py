"""
loader.py

Loads website content using LangChain WebBaseLoader.
"""

from langchain_community.document_loaders import WebBaseLoader
from crawler.utils import clean_text


class WebsiteLoader:
    def __init__(self, url: str):
        self.url = url

    def load(self):
        """
        Load website documents.

        Returns:
            List[Document]
        """
        try:
            loader = WebBaseLoader(self.url)
            documents = loader.load()

            # Clean document text
            for doc in documents:
                doc.page_content = clean_text(doc.page_content)

            return documents

        except Exception as e:
            raise Exception(f"Error loading website: {e}")