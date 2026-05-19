import logging
import sys
from blogservicepkg.config import settings

def setup_logging():

    root_logger = logging.getLogger()
    root_logger.setLevel(settings.LOG_LEVEL)

    # IMPORTANT: ensure handler exists
    if not root_logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(settings.LOG_LEVEL)
        root_logger.addHandler(handler)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    #set formatter for handlers.
    for handler in root_logger.handlers:
        handler.setFormatter(formatter)    

    #logging.getLogger("botocore").setLevel(logging.WARNING)
    #logging.getLogger("boto3").setLevel(logging.WARNING)