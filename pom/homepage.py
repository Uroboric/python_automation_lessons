from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import SeleniumBase
from typing import List


class HomepageNav(SeleniumBase):

    # CSS locators
    categories = '.c_320-menu-links-list'
    category = '.c_320-build_cta-long'

    # Return all categories WebElements except Build_And_Price
    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.categories, 'Vehicles,Shop At Home,Discover Nissan,Owners,Locate Dealer')

    # Return a Build_And_Price WebElement
    def get_category(self) -> WebElement:
        return self.is_visible('css', self.category, 'Build & Price')

    # Methods for getting the text of each title button
    def get_nav_links_text(self) -> List[str]:
        nav_links = self.get_nav_links()
        nav_links_text = [link.text for link in nav_links]
        return ",".join(nav_links_text).split('\n')

    # Method for getting the text of Build & Price button
    def get_nav_link_text(self) -> str:
        nav_link_text = self.get_category().text
        return nav_link_text
