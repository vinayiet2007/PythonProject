import time
import pytest
from sampleProject.ui.pages.login_page import LoginPage


@pytest.mark.description("****Test Case 1******")
def test_login(setup_driver):
    """
    Verify Sauce Demo Login
    """
    driver = setup_driver
    login_page = LoginPage(driver,"login_page")
    login_page.enter_user_name("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.login()
    current_url = driver.current_url
    assert "inventory.html" in current_url
    time.sleep(2)