'''conftest.py: This is a local plugin that allows you to connect hook functions and fixtures to the directory
where the conftest.py file exists, and all of its subdirectories.
In other words, it contains configurations for our tests.'''


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('--headless')
    options.add_argument('chrome')
    options.add_argument('user-agent=[Mozilla/5.0 (X11; Linux x86_64; Ubuntu 22.04) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36]')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.nissanusa.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
