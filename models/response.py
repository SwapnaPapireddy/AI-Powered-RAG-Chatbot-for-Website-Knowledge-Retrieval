"""
response.py

Pydantic response models.
"""

from pydantic import BaseModel
from typing import List


class WebsiteResponse(BaseModel):
    """
    Response after website processing.
    """
    status: str
    message: str
    documents_loaded: int
    chunks_created: int


class ChatResponse(BaseModel):
    """
    Response returned by chatbot.
    """
    question: str
    answer: str


class SourceResponse(BaseModel):
    """
    Source document returned by retriever.
    """
    source: str
    content: str


class ErrorResponse(BaseModel):
    """
    Error response.
    """
    status: str
    error: str


class HistoryResponse(BaseModel):
    """
    Chat history response.
    """
    history: List[str]