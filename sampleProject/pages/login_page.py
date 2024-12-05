from common.ui.browser_events.browser_events import BrowserEvents
from common.ui.resource_manager.elements import Elements
from sampleProject.pages.common_functions.fetch_element import FetchElement


class LoginPage:
    def __init__(self,driver,resource_name):
        self.driver=driver
        self.login_resource=FetchElement(resource_name)
        self.element_page = Elements(self.driver)
        self.browser_event = BrowserEvents(self.driver)

    def enter_user_name(self,user_name_value:str):
        user_name_locator = self.login_resource.fetch_element_from_json("user_name_text")
        user_name_element = self.element_page.get_element(user_name_locator)
        self.browser_event.set_text(user_name_element,user_name_value)

    def enter_password(self,password:str):
        password_locator = self.login_resource.fetch_element_from_json("password_text")
        password_element = self.element_page.get_element(password_locator)
        self.browser_event.set_text(password_element,password)

    def login(self):
        login_button_locator = self.login_resource.fetch_element_from_json("login_button")
        login_button_element = self.element_page.get_element(login_button_locator)
        self.browser_event.click(login_button_element)