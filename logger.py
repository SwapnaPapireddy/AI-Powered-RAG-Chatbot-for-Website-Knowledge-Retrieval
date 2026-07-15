"""
logger.py

Application logger.
"""

import logging
import os

from config.settings import Settings


class Logger:

    @staticmethod
    def get_logger(name: str):

        os.makedirs("logs", exist_ok=True)

        logger = logging.getLogger(name)

        logger.setLevel(Settings.LOG_LEVEL)

        if not logger.handlers:

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            )

            # Console Handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            # File Handler
            file_handler = logging.FileHandler(
                "logs/rag_chatbot.log"
            )
            file_handler.setFormatter(formatter)

            logger.addHandler(console_handler)
            logger.addHandler(file_handler)

        return logger