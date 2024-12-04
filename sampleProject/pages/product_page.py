from common.browserEvents.browserEvents import BrowserEvents
from common.resourseManager.elements import Elements
from sampleProject.pages.common_functions.fetch_element import FetchElement


class ProductPage:
    def __init__(self,driver,resource_name):
        self.driver=driver
        self.login_resource=FetchElement(resource_name)
        self.element_page = Elements(self.driver)
        self.browser_event = BrowserEvents(self.driver)

    def find_products(self):
        products_title_locator = self.login_resource.fetch_element_from_json("products_title")
        products_title_element = self.element_page.get_elements(products_title_locator)
        print(len(products_title_element))
        return len(products_title_element)

    def find_products_title(self):
        products_title_locator = self.login_resource.fetch_element_from_json("products_title")
        product_elements = self.element_page.get_elements(products_title_locator)
        return [product_element.text for product_element in product_elements]

    def sort_products(self,sort_option):
        sort_product_select_locator = self.login_resource.fetch_element_from_json("sort_product_select")
        sort_product_select_locator_element = self.element_page.get_element(sort_product_select_locator)
        self.browser_event.select_option(sort_product_select_locator_element,sort_option)
