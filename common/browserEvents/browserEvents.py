from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webelement import WebElement
from common.utilities.logger import Logger

from common.interfaces.iBrowserEvents import IBrowserEvents

class BrowserEvents(IBrowserEvents):
    driver: webdriver

    def __init__(self,driver:webdriver):
        self.driver=driver

    def set_text(self,element:WebElement,text:str):
        element.send_keys(text)
        Logger.info(f"Successfully Type value '{text}'")

    def get_text(self,element:WebElement):
        fetched_value = element.text
        Logger.info(f"Successfully fetched from element : {fetched_value}")
        return fetched_value

    def click(self,element:WebElement):
        element.click()
        Logger.info(f"Successfully clicked on element")

    def get_attribute(self, element: WebElement,attribute:str):
        attribute_value = element.value_of_css_property(attribute)
        Logger.info(f"Successfully fetched attribute: '{attribute}' value: '{attribute_value}'")
        return attribute_value

    def select_option(self, element: WebElement,option:str):
        select = Select(element)
        select.select_by_value(option)
        Logger.info(f"Successfully selected option: '{option}'")