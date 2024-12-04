
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.firefox import GeckoDriverManager
from common.utilities.logger import Logger
# import urllib3
# urllib3.util.timeout.Timeout(connect=60.0, read=120.0)

class Driver:

    driver :None
    @staticmethod
    def driver_setup(browser_name,timeout=10000):
        try:
            Logger.info(f"Application will run in : {browser_name}")
            options = ChromeOptions()
            match browser_name:
                case 'chrome':
                    # options.add_argument("--headless")
                    options.add_argument("--disable-gpu")
                    service = ChromeService(ChromeDriverManager().install())
                    Driver.driver = webdriver.Chrome(service=service, options=options)
                    Driver.driver.set_page_load_timeout(timeout)
                case 'firefox':
                    service = FirefoxService(GeckoDriverManager().install())
                    Driver.driver = webdriver.Firefox(service=service)
                case 'safari':
                    pass
                case _:
                    pass
            Driver.driver.maximize_window()
            return Driver.driver
        except WebDriverException:
            Logger.critical(f"No Driver found {WebDriverException}")
        except Exception as e:
            Logger.critical(f"No Driver found {e}")

    @staticmethod
    def navigate_url(url):
        Driver.driver.get(url)

    @staticmethod
    def driver_close():
        Logger.info(f"Driver is closed")
        Driver.driver.close()

    @staticmethod
    def driver_quit():
        Logger.info(f"Driver is quit")
        Driver.driver.quit()
