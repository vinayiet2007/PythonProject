from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.webkitgtk.webdriver import WebDriver
from common.ui.baseClasses.driver import Driver
from common.ui.interfaces.iElements import IElements
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from common.ui.resourseManager.resourseManager import ResourceManager
from common.utilities.logger import Logger

class Elements(IElements):

    def __init__(self,driver:WebDriver):
        self.driver = driver

    def get_element(self, locator_object):
        try:
            element:WebElement
            resource_manager = ResourceManager()
            resource_object = resource_manager.fetchElement(locator_object)
            locator_type = resource_object[0]
            locator_value = resource_object[1]
            Logger.info(f"Searching for Locator with type and value: {locator_type} - {locator_value}")
            match locator_type:
                case 'xpath':
                    element = self.driver.find_element(By.XPATH, locator_value)
                case 'css':
                    element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
                case 'id':
                    element = self.driver.find_element(By.ID, locator_value)
                case _:
                    return "no Element found"
            Logger.info(f"Element found with Locator type and value: {locator_type} - {locator_value}")
            return element
        except NoSuchElementException:
            Logger.critical(f"No Element found : {NoSuchElementException}")
        except TimeoutException:
            Logger.critical(f"No Element found in given time: {TimeoutException}")

    def get_elements(self, locator_object):
        try:
            elements:[WebElement]
            resource_manager = ResourceManager()
            resource_object = resource_manager.fetchElement(locator_object)
            locator_type = resource_object[0]
            locator_value = resource_object[1]
            Logger.info(f"Searching for Locator with type and value: {locator_type} - {locator_value}")
            match locator_type:
                case 'xpath':
                    elements = self.driver.find_elements(By.XPATH, locator_value)
                case 'css':
                    elements = self.driver.find_elements(By.CSS_SELECTOR, locator_value)
                case 'id':
                    elements = self.driver.find_elements(By.ID, locator_value)
                case _:
                    return "no Element found"
            Logger.info(f"Element found with Locator type and value: {locator_type} - {locator_value}")
            return elements
        except NoSuchElementException:
            Logger.critical(f"No Element found : {NoSuchElementException}")
        except TimeoutException:
            Logger.critical(f"No Element found in given time: {TimeoutException}")

    def get_locator(self, locator_object):
        try:
            resource_manager = ResourceManager()
            resource_object = resource_manager.fetchElement(locator_object)
            locator_type = resource_object[0]
            locator_value = resource_object[1]
            Logger.info(f"Searching for Locator with type and value: {locator_type} - {locator_value}")
            match locator_type:
                case 'xpath':
                    return By.XPATH, locator_value
                case 'css':
                    return By.CSS_SELECTOR, locator_value
                case 'id':
                    return By.ID, locator_value
                case _:
                    return "no Locator found"
        except NoSuchElementException:
            Logger.critical(f"Locator not found : {NoSuchElementException}")
        except TimeoutException:
            Logger.critical(f"No Locator found in given time: {TimeoutException}")

if __name__=='__main__':
    test = {
        "locator_type": "xpath",
        "locator_value": "//test"
    }
    Logger.info("Test Application")
    Driver.driver_setup(browser_name="chrome")