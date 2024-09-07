import logging

logging.basicConfig(
    level=logging.CRITICAL,
    format="[%(name)s] %(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S")

def get_logger(name):
    logger =  logging.getLogger(name)
    logger.setLevel(logging.INFO)

    return logger