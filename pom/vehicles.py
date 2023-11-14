import allure
from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import SeleniumBase


@allure.suite("Vehicles Navigation test")
class VehiclesNav(SeleniumBase):
    # Vehicles button
    button_vehicles = 'button[aria-controls="c_320B-panel-Vehicles"]'
#xpath //button[@aria-controls="c_320B-panel-Vehicles"]
    # Car mappings
    car_mapping = {
        'Ariya': {
            'link_selector': '#categoryPanel_Crossovers-and-SUVs_0 [data-vehicle-name="Nissan ARIYA"]',
            'price_selector': '.col-12 .c_349-pricing-msrp'
        },
        'Kicks': {
            'link_selector': '#categoryPanel_Crossovers-and-SUVs_0 [href="/vehicles/crossovers-suvs/kicks.html"]',
            'price_selector': '.col-12 .c_349-pricing-msrp'
        },
        'Rogue Sport': {
            'link_selector': '#categoryPanel_Crossovers-and-SUVs_0 [href="/vehicles/crossovers-suvs/rogue-sport.html"]',
            'price_selector': '.col-12 .c_349-pricing-msrp'
        },
        'Rogue': {
            'link_selector': '#categoryPanel_Crossovers-and-SUVs_0 [href="/vehicles/crossovers-suvs/rogue.html"]',
            'price_selector': '.col-12 .js-sub-model-price'
        },
        'Murano': {
            'link_selector': '#categoryPanel_Crossovers-and-SUVs_0 [href="/vehicles/crossovers-suvs/murano.html"]',
            'price_selector': '.col-12 .c_349-pricing-msrp'
        },
        'Pathfinder': {
            'link_selector': '#categoryPanel_Crossovers-and-SUVs_0 [href="/vehicles/crossovers-suvs/pathfinder.html"]',
            'price_selector': '.col-12 .c_349-pricing-msrp'
        },
        'Armada': {
            'link_selector': '#categoryPanel_Crossovers-and-SUVs_0 [href="/vehicles/crossovers-suvs/armada.html"]',
            'price_selector': '.col-12 .c_349-pricing-msrp'
        }
    }

    @allure.title("Return a Vehicles button is present")
    def get_button_to_be_clickable(self) -> WebElement:
        return self.is_present('css', self.button_vehicles, 'Vehicles button is not clickable')

    @allure.title("Return a Vehicles button is present")
    def get_button_vehicles_present(self) -> WebElement:
        return self.is_present('css', self.button_vehicles, 'Vehicles button is not present')

    @allure.title("Return a Vehicles button is visible")
    def get_button_vehicles_visible(self) -> WebElement:
        return self.is_visible('css', self.button_vehicles, 'Vehicles button is not visible')

    @allure.title("Return a car link element based on car_name")
    def get_car_link(self, car_name) -> WebElement:
        return self.is_visible('css', self.car_mapping[car_name]['link_selector'], f'{car_name} link')

    @allure.title("Return a car price element based on car_name")
    def get_car_price(self, car_name) -> WebElement:
        return self.is_visible('css', self.car_mapping[car_name]['price_selector'], f'{car_name} price')

    @allure.title("Method for getting the text of a car price based on car_name")
    def get_car_price_text(self, car_name):
        return self.get_car_price(car_name).text
