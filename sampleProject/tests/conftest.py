import pytest
from common.baseClasses.driver import Driver
import time

from sampleProject.pages.login_page import LoginPage


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    test_fn = item.obj
    docstring = getattr(test_fn, '__doc__')
    if docstring:
        report.nodeid = docstring

@pytest.fixture
def setup_driver():
    driver = Driver.driver_setup('chrome')
    Driver.navigate_url('https://www.saucedemo.com/')
    yield driver
    Driver.driver_close()

@pytest.fixture
def login(setup_driver):
    driver = setup_driver
    login_page = LoginPage(driver,"login_page")
    login_page.enter_user_name("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.login()
    yield driver

