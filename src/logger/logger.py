import logging


def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # File handler
        fh = logging.FileHandler("logger/scraper.log", encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # Formatter
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # Add handlers
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger
