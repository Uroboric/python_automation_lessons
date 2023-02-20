'''conftest.py: This is a local plugin that allows you to connect hook functions and fixtures to the directory
where the conftest.py file exists, and all of its subdirectories.
In other words, it contains configurations for our tests.'''


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver



@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Use headless if you do not need a browser UI
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1650,900')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(executable_path='C:\Сhromedriver', options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    driver = EventFiringWebDriver(driver)
    url = 'https://www.nissanusa.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()