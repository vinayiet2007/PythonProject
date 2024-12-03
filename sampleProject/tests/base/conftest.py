import pytest
from common.baseClasses.driver import Driver
import time

@pytest.fixture
def setup_driver():
    driver = Driver.driver_setup('chrome')
    time.sleep(10)
    yield driver
    Driver.driver_quit()