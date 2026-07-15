"""
helper.py

Common helper functions used across the project.
"""

import os
from typing import List


def ensure_directory(directory: str):
    """
    Create directory if it doesn't exist.
    """
    os.makedirs(directory, exist_ok=True)


def format_documents(documents) -> str:
    """
    Convert LangChain documents into a single string.
    """

    if not documents:
        return ""

    return "\n\n".join(
        doc.page_content for doc in documents
    )


def get_document_count(documents) -> int:
    """
    Return total number of documents.
    """
    return len(documents)


def get_chunk_count(chunks) -> int:
    """
    Return total number of chunks.
    """
    return len(chunks)


def print_separator(length=60):
    """
    Print separator line.
    """
    print("=" * length)


def truncate_text(text: str, max_length: int = 300):
    """
    Truncate long text.
    """

    if len(text) <= max_length:
        return text

    return text[:max_length] + "..."


def preview_chunks(chunks, num_chunks=3):
    """
    Print first few chunks.
    """

    print_separator()

    print(f"Previewing {num_chunks} Chunks\n")

    for index, chunk in enumerate(chunks[:num_chunks], start=1):

        print(f"Chunk {index}")
        print("-" * 50)

        print(truncate_text(chunk.page_content))

        print()

    print_separator()


def validate_url(url: str):
    """
    Basic URL validation.
    """

    return (
        url.startswith("http://")
        or url.startswith("https://")
    )