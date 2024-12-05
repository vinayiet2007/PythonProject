from abc import ABC,abstractmethod

class IResourceManager(ABC):

    @abstractmethod
    def fetchElement(self,resource_json):
        pass
