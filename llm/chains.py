"""
chains.py

Creates the RAG chain.
"""

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from llm.prompt import RAG_PROMPT


class RAGChain:

    def __init__(self, llm, retriever):

        self.llm = llm
        self.retriever = retriever

    def format_docs(self, docs):

        return "\n\n".join(
            doc.page_content
            for doc in docs
        )

    def build_chain(self):

        chain = (
            {
                "context": self.retriever | self.format_docs,
                "question": RunnablePassthrough(),
                "chat_history": lambda _: ""
            }
            | RAG_PROMPT
            | self.llm
            | StrOutputParser()
        )

        return chain