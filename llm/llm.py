"""
llm.py

Loads the LLM (Google Gemini).
"""

from langchain_google_genai import ChatGoogleGenerativeAI

from config.settings import Settings


class LLMModel:

    def __init__(
        self,
        model_name=Settings.LLM_MODEL,
        temperature=Settings.TEMPERATURE
    ):
        self.model_name = model_name
        self.temperature = temperature

    def load(self):

        llm = ChatGoogleGenerativeAI(
            model=self.model_name,
            google_api_key=Settings.GOOGLE_API_KEY,
            temperature=self.temperature
        )

        return llm