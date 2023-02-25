from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Homepage:

    # CSS locators for header buttons
    Vehicles = (By.CSS_SELECTOR, 'li.c_320-menu-links-list-item--primary:nth-child(1) > button:nth-child(1) > span:nth-child(1)')
    Shop_At_Home = (By.CSS_SELECTOR, 'li.c_320-menu-links-list-item--primary:nth-child(2) > button:nth-child(1)')
    Discover_Nissan = (By.CSS_SELECTOR, 'li.c_320-menu-links-list-item:nth-child(3) > button:nth-child(1)')
    Owners = (By.CSS_SELECTOR, '#c_320-panel--link-list-dropdown-more > ul > li:nth-child(1) > button')
    Locate_Dealer = (By.CSS_SELECTOR, '#c_320-panel--link-list-dropdown-more > ul > li:nth-child(2) > button')
    Build_And_Price = (By.CSS_SELECTOR, '.c_320-build_cta-long')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5, 0.3)

# Methods for getting a WebElement for each header button
    def get_vehicles(self):
        return self.wait.until(ec.element_to_be_clickable(self.Vehicles))

    def get_shop_at_home(self):
        return self.wait.until(ec.element_to_be_clickable(self.Shop_At_Home))

    def get_discover_nissan(self):
        return self.wait.until(ec.element_to_be_clickable(self.Discover_Nissan))

    def get_owners(self):
        return self.wait.until(ec.element_to_be_clickable(self.Owners))

    def get_locate_dealer(self):
        return self.wait.until(ec.element_to_be_clickable(self.Locate_Dealer))

    def get_build_and_price(self):
        return self.wait.until(ec.element_to_be_clickable(self.Build_And_Price))

# Methods for getting the text of each title button
    def get_vehicles_text(self):
        return self.get_vehicles().text

    def get_shop_at_home_text(self):
        return self.get_shop_at_home().text

    def get_discover_nissan_text(self):
        return self.get_discover_nissan().text

    def get_owners_text(self):
        return self.get_owners().text

    def get_locate_dealer_text(self):
        return self.get_locate_dealer().text

    def get_build_and_price_text(self):
        return self.get_build_and_price().text
