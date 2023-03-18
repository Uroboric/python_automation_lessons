from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import SeleniumBase
from typing import List


class HomepageNav(SeleniumBase):

    # CSS locators
    nav_links = '.c_320-menu-links-list[role="menubar"]'
    build_price_link = '.c_320-build_cta-long'

    # Return all categories WebElements except Build_And_Price
    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.nav_links, 'Vehicles,Shop At Home,Discover Nissan,Owners,Locate Dealer')

    # Return a Build_And_Price WebElement
    def get_build_price_link(self) -> WebElement:
        return self.is_visible('css', self.build_price_link, 'Build & Price')

    # Method for getting the text of each title button
    def get_nav_links_text(self) -> List[str]:
        return self.get_nav_links()[-1].text.split('\n')

    # Method for getting the text of Build & Price button
    def get_build_price_text(self) -> str:
        return self.get_build_price_link().text
