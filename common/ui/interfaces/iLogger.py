from abc import ABC,abstractmethod

class ILogger(ABC):

     @staticmethod
     @abstractmethod
     def info(message:str):
         pass

     @staticmethod
     @abstractmethod
     def debug(message: str):
         pass

     @staticmethod
     @abstractmethod
     def warn(message: str):
         pass

     @staticmethod
     @abstractmethod
     def critical(message: str):
         pass