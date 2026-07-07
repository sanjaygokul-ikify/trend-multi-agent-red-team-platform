import logging

LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

def setup_logging():
    logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)