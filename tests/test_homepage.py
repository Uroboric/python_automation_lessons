import time

import pytest
from selenium import webdriver


@pytest.mark.usefixtures('setup')
class TestHomepage:


    def test_homepage(self):
        time.sleep(5)
        pass
