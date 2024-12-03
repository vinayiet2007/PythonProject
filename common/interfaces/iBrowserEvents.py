from abc import ABC,abstractmethod

from selenium.webdriver.remote.webelement import WebElement


class IBrowserEvents(ABC):

    @abstractmethod
    def click(self,element:WebElement):
        pass

    @abstractmethod
    def set_text(self,element:WebElement,text:str):
        pass

    @abstractmethod
    def get_text(self,element:WebElement):
        pass

    @abstractmethod
    def get_attribute(self, element: WebElement,attribute:str):
        pass

    @abstractmethod
    def select_option(self, element: WebElement,option:str):
        pass


