import logging
from common.constants import LOG_FORMATTER

logger = None
std_log_file_path = '/var/log/fizzbuzz/Info_log.log'


def _set_logger():
    global logger
    handler = logging.FileHandler(std_log_file_path)
    formatter = logging.Formatter(LOG_FORMATTER)
    handler.setFormatter(formatter)

    logger = logging.getLogger('py_logger')
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


_set_logger()
