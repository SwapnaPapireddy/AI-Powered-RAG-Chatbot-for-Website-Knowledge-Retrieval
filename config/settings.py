"""
settings.py

Centralized configuration settings for the RAG chatbot.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Settings:
    """
    Application settings.
    """

    # ===========================
    # API KEYS
    # ===========================

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    # ===========================
    # WEBSITE
    # ===========================

    REQUEST_TIMEOUT = 30

    # ===========================
    # TEXT SPLITTING
    # ===========================

    CHUNK_SIZE = 1000

    CHUNK_OVERLAP = 200

    # ===========================
    # EMBEDDING MODEL
    # ===========================

    EMBEDDING_MODEL = (
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    # ===========================
    # VECTOR DATABASE
    # ===========================

    VECTOR_DB_PATH = "embeddings/faiss_index"

    TOP_K = 4

    # ===========================
    # LLM
    # ===========================

    LLM_MODEL = "gemini-2.5-flash"

    TEMPERATURE = 0.3

    MAX_OUTPUT_TOKENS = 1024

    # ===========================
    # STREAMLIT
    # ===========================

    PAGE_TITLE = "Website RAG Chatbot"

    PAGE_ICON = "🤖"

    # ===========================
    # FASTAPI
    # ===========================

    HOST = "127.0.0.1"

    PORT = 8000

    # ===========================
    # LOGGING
    # ===========================

    LOG_LEVEL = "INFO"