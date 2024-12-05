from abc import ABC,abstractmethod
from selenium.webdriver.remote.webelement import WebElement

class IWait(ABC):

    @abstractmethod
    def wait_for_element_to_visible(self,element_locator):
        pass

    @abstractmethod
    def wait_for_element_to_be_invisible(self,element_locator):
        pass

    @abstractmethod
    def element_to_be_clickable(self,element_locator):
        pass

    @abstractmethod
    def no_of_windows(self,timeout,number_of_windows:int):
        pass