import types
from functools import wraps
from PyQt5.QtCore import pyqtSlot
from injector import inject
from ..logger import logger

__all__ = ['slot', 'inject']

def slot(*args):
    if len(args) == 1 and isinstance(args[0], types.FunctionType):
        func = args[0]
        args = []
    else:
        func = None

    def slot_decorator(func):
        @pyqtSlot(*args)
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                logger.add_error(e)
        return wrapper

    if func is not None:
        return slot_decorator(func)
    else:
        return slot_decorator