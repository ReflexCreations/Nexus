from . import logger
import os

__all__ = ['load', 'file_exists']

def load(self, file_name):
    #if self.file_exists(file_name
        with open(file_name, 'r') as f:
            return f.read()
      
def file_exists(self, file_name):
    return os.path.isfile(file_name)