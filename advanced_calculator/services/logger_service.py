import logging
from pathlib import Path


class LoggerService:
    """Centralized application logging."""

    def __init__(self, path="data/app.log"):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        logging.basicConfig(
            filename=path,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )
        self.logger = logging.getLogger("advanced_calculator")

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)
