from abc import ABC,abstractmethod

class IElements(ABC):

    @abstractmethod
    def get_element(self,locator_object):
        pass

    @abstractmethod
    def get_locator(self, locator_object):
        pass