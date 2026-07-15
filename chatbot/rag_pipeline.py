"""
rag_pipeline.py

Complete RAG Pipeline
"""

from llm.llm import LLMModel
from llm.prompt import RAG_PROMPT, GENERAL_PROMPT, INTENT_PROMPT
from chatbot.memory import ChatMemory


class RAGPipeline:

    def __init__(self, retriever):

        self.retriever = retriever

        self.memory = ChatMemory()

        self.llm = LLMModel().load()

    def format_documents(self, docs):

        return "\n\n".join(
            doc.page_content
            for doc in docs
        )

    def classify_intent(self, question):
        """
        Decide whether the question is general conversation
        (greetings, thanks, small talk) or a document-specific
        question that needs retrieval from the loaded website.

        Returns "GENERAL" or "DOCUMENT".
        """

        prompt = INTENT_PROMPT.invoke({
            "question": question
        })

        response = self.llm.invoke(prompt)

        intent = response.content.strip().upper()

        if "GENERAL" in intent:
            return "GENERAL"

        return "DOCUMENT"

    def ask(self, question):

        # Load chat history (shared by both paths)
        chat_history = self.memory.load_memory()

        intent = self.classify_intent(question)

        if intent == "GENERAL":

            # Small talk / greetings - answer directly, no retrieval
            prompt = GENERAL_PROMPT.invoke({
                "question": question,
                "chat_history": chat_history
            })

            response = self.llm.invoke(prompt)

            answer = response.content

        else:

            # Document-specific question - retrieve then answer
            docs = self.retriever.invoke(question)

            context = self.format_documents(docs)

            prompt = RAG_PROMPT.invoke({
                "context": context,
                "question": question,
                "chat_history": chat_history
            })

            response = self.llm.invoke(prompt)

            answer = response.content

        # Save conversation
        self.memory.save_context(
            question,
            answer
        )

        return answer

    def reset_chat(self):

        self.memory.clear_memory()