from abc import ABCMeta,abstractmethod

class Male(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def send_flower(self):
        pass

    @abstractmethod
    def send_chocolate(self):
        pass

    @abstractmethod
    def send_book(self):
        pass
