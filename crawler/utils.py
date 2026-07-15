"""
utils.py

Utility functions for crawler.
"""

import re


def clean_text(text: str) -> str:
    """
    Clean website text.

    Args:
        text: Raw webpage text

    Returns:
        Cleaned text
    """

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove multiple blank lines
    text = re.sub(r"\n+", "\n", text)

    return text.strip()


def print_document_stats(documents):
    """
    Print document statistics.

    Args:
        documents: List[Document]
    """

    print("=" * 60)
    print(f"Number of Documents : {len(documents)}")

    total_chars = sum(len(doc.page_content) for doc in documents)

    print(f"Total Characters    : {total_chars}")
    print("=" * 60)


def preview_documents(documents, num_docs=2):
    """
    Print first few document previews.
    """

    for i, doc in enumerate(documents[:num_docs]):
        print(f"\nDocument {i + 1}")
        print("-" * 40)
        print(doc.page_content[:500])
        print("-" * 40)