import logging
import sys


def get_handler():
    simple_formatter = logging.Formatter(
        fmt="%(asctime)s-%(name)s-[%(levelname)s]-%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    handler.setFormatter(simple_formatter)
    return handler


def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_handler())
    return logger