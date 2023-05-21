from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def lock_access(self, pad):
        pass

    @abstractmethod
    def unlock_access(self, pad):
        pass