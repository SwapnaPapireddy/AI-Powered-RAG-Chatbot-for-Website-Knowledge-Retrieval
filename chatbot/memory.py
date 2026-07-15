"""
memory.py

Conversation Memory

NOTE: ConversationBufferMemory was removed from langchain.memory
in LangChain 1.0 (it was deprecated since v0.3.1). Rather than
depend on LangChain's shifting memory APIs, this stores chat
history directly as a plain string, formatted for use in the
prompt template in llm/prompt.py.
"""


class ChatMemory:

    def __init__(self):

        self._history = []  # list of (question, answer) tuples

    def load_memory(self):
        """
        Returns the conversation history as a single formatted
        string, ready to drop into the {chat_history} slot of
        the prompt template.
        """

        if not self._history:
            return ""

        lines = []

        for question, answer in self._history:
            lines.append(f"User: {question}")
            lines.append(f"Assistant: {answer}")

        return "\n".join(lines)

    def save_context(self, question, answer):

        self._history.append((question, answer))

    def clear_memory(self):

        self._history = []