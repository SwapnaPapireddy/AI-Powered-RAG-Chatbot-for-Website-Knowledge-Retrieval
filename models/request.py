"""
request.py

Pydantic request models.
"""

from pydantic import BaseModel, HttpUrl


class URLRequest(BaseModel):
    """
    Request model for loading a website.
    """
    url: HttpUrl


class ChatRequest(BaseModel):
    """
    Request model for asking questions.
    """
    question: str


class ResetRequest(BaseModel):
    """
    Request model for clearing chat memory.
    """
    reset: bool = True