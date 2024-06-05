'''conftest.py: This is a local plugin that allows you to connect hook functions and fixtures to the directory
where the conftest.py file exists, and all of its subdirectories.
In other words, it contains configurations for our tests.'''
# from datetime import datetime
# import allure
# import pytest
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
#
#
# @pytest.fixture
# def get_firefox_options():
#     options = FirefoxOptions()
#     options.add_argument('--headless')
#     options.add_argument('--user-agent=[Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0')
#     options.add_argument('--window-size=1920,1080')
#     options.add_argument('--start-maximized')
#     return options
#
# @pytest.fixture
# def get_webdriver(get_firefox_options):
#     options = get_firefox_options
#     service = FirefoxService(GeckoDriverManager().install())
#     driver = webdriver.Firefox(options=options, service=service)
#     return driver
#
#
# @pytest.fixture(scope='function')
# def setup(request, get_webdriver):
#     driver = get_webdriver
#     url = 'https://www.nissanusa.com/'
#     if request.cls is not None:
#         request.cls.driver = driver
#         driver.get(url)
#     yield driver
#     screenshot_data = driver.get_screenshot_as_png()
#     allure.attach(screenshot_data, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
#     driver.quit()

# CHROME SETTINGS
from datetime import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    # options.add_argument('--headless')
    options.add_argument('--user-agent=[Mozilla/5.0 (X11; Linux x86_64; Ubuntu 22.04) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.90 Safari/537.36]')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--start-maximized')
    return options

#for webdriver(localy)
# @pytest.fixture
# def get_webdriver(get_chrome_options):
#     options = get_chrome_options
#     driver = webdriver.Chrome(options=options)
#     return driver
@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "124.0",
        "selenoid:options": {
            "enableVNC": True,
        }
    }
    driver = webdriver.Remote(
        command_executor='http://0.0.0.0:8080/wd/hub',
        options=options,
        desired_capabilities=capabilities
    )
    return driver



@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.nissanusa.com/'
    if request.cls is not None:
        request.cls.driver = driver
    else:
        return "driver is not initialized"
    driver.get(url)
    yield driver
    screenshot_data = driver.get_screenshot_as_png()
    allure.attach(screenshot_data, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()
