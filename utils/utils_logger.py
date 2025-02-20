import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(message):
    """Log an info-level message."""
    logging.info(message)

def log_error(message):
    """Log an error-level message."""
    logging.error(message)
