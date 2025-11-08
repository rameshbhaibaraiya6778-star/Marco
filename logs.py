# logs.py


import logging
from logging.handlers import TimedRotatingFileHandler


def setup_logger(name="main", level=logging.INFO):
    """Create and configure a daily rotating logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Define log format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
        "%d-%b-%y %H:%M:%S"
    )

    # Daily rotation at midnight, keep logs for 7 days
    file_handler = TimedRotatingFileHandler(
        "logs.txt",
        when="midnight",
        interval=1,
        backupCount=7,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    # Stream to console as well
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Avoid duplicate handlers if re-imported
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    # Reduce noise from other libraries
    logging.getLogger("pyrogram").setLevel(logging.WARNING)

    return logger


# Initialize main logger
logger = setup_logger(level=logging.ERROR)

# Example usage (optional)
if __name__ == "__main__":
    logger.info("Logger initialized successfully.")
    logger.error("This is a sample error log.")
