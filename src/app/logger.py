import logging


class Logger():
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    formatter = logging.Formatter(format)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    def __new__(cls, name, level=logging.WARNING):
        logger = logging.getLogger(name)
        logger.addHandler(cls.handler)
        logger.setLevel(level)
        return logger
