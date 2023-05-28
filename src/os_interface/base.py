import abc

class Base(abc.ABC):
    @abc.abstractmethod
    def lock_access(self, pad):
        pass

    @abc.abstractmethod
    def unlock_access(self, pad):
        pass