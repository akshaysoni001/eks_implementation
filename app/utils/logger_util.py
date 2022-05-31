"""Module to handle logging functionality"""
import logging
import os
import sys


def get_logger(logger_name, file_name, console_logs=False):
    logger = logging.getLogger(logger_name)
    file_handler = logging.FileHandler(file_name)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    file_handler.setFormatter(formatter)
    # add file handler to logger
    logger.addHandler(file_handler)
    logger.setLevel(os.environ.get('LOG_LEVEL', 'DEBUG'))
    if console_logs:
        console_handle = logging.StreamHandler(sys.stdout)
        console_handle.setFormatter(formatter)
        logger.addHandler(console_handle)
    return logger


def get_process_logger(process_name, root_logger):
    file_handler = logging.FileHandler("%s.log" % process_name)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)
    return root_logger


logger = get_logger("EKS Service Logger", "Main.log", True)
