from common.interfaces.iWait import IWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Wait(IWait):

    def __init__(self,driver):
        self.driver = driver

    def wait_for_element_to_visible(self,element_locator):
        try:
            WebDriverWait(self.driver, timeout=10000).until(EC.visibility_of_element_located(element_locator))
        except Exception as e:
            print(f" Error in waiting for element - Error = {e}")

    def wait_for_element_to_be_invisible(self,element_locator):
        try:
            WebDriverWait(self.driver, timeout=10000).until(EC.invisibility_of_element(element_locator))
        except Exception as e:
            print(f" Error in waiting for element to be invisible- Error = {e}")

    def element_to_be_clickable(self,element_locator):
        try:
            WebDriverWait(self.driver, timeout=10000).until(EC.element_to_be_clickable(element_locator))
        except Exception as e:
            print(f" Error in waiting for element to be clickable - Error = {e}")

    def no_of_windows(self, timeout,number_of_windows:int):
        try:
            WebDriverWait(self.driver, timeout=10000).until(EC.number_of_windows_to_be(number_of_windows))
        except Exception as e:
            print(f" Error in waiting for no of windows to be {number_of_windows} - Error = {e}")
