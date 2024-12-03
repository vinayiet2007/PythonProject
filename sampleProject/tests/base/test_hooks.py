import pytest
from common.baseClasses.driver import Driver
import time
from common.utilities.logger import Logger

def test_url(setup_driver):
    driver = setup_driver
    Driver.navigate_url('https://www.saucedemo.com/')
    url=driver.current_url
    Logger.info(f"Current URL is === {url}")
    assert "saucedemo" in url