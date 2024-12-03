from abc import ABC,abstractmethod

class IDriver(ABC):

    @abstractmethod
    def setUp(self,browser_name):
        pass

    @abstractmethod
    def navigate(self,url):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def quit(self):
        pass