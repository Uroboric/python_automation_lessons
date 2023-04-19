from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import SeleniumBase


class HomepageNav(SeleniumBase):
    # CSS locators
    button_crossovers_and_SUVs = '.c_310_tertiary_grid_slider button[data-bodystyle="Crossovers & SUVs"] .c_310-vehicles-count'
    cars_in_crossovers_and_SUVs = '#vehiclelist--1738608765_categoryPanel_0 .c_310-1'

    click_cars = '.c_310_tertiary_grid_slider [data-label="Cars"]'
    button_cars = '.c_310_tertiary_grid_slider button[data-bodystyle="Cars"] .c_310-vehicles-count'
    cars_in_cars = '#vehiclelist--1738608765_categoryPanel_1 .c_310-1'

    click_electic = '.c_310_tertiary_grid_slider button[data-bodystyle="Electric"]'
    button_electric = '.c_310_tertiary_grid_slider button[data-bodystyle="Electric"] .c_310-vehicles-count'
    cars_in_electric = '#vehiclelist--1738608765_categoryPanel_2 .c_310-1'

    click_sports_cars = '.c_310_tertiary_grid_slider button[data-bodystyle="Sports Cars"]'
    button_sports_cars = '.c_310_tertiary_grid_slider button[data-bodystyle="Sports Cars"] .c_310-vehicles-count'
    cars_in_sports_cars = '#vehiclelist--1738608765_categoryPanel_3 .c_310-1'

    click_trucks = '.c_310_tertiary_grid_slider button[data-bodystyle="Trucks"]'
    button_trucks = '.c_310_tertiary_grid_slider button[data-bodystyle="Trucks"] .c_310-vehicles-count'
    cars_in_trucks = '#vehiclelist--1738608765_categoryPanel_4 .c_310-1'

    '''Crossovers & SUVs'''

    # Return a Crossovers & SUVs tab
    def get_category_crossovers_and_SUVs(self) -> WebElement:
        return self.is_visible('css', self.button_crossovers_and_SUVs, 'Crossovers & SUVs')

    # Method for getting the text of Crossovers & SUVs tab
    def get_category_crossovers_and_SUVs_text(self):
        return self.get_category_crossovers_and_SUVs().text

    # Return number of cars displayed on Crossovers & SUVs grid pannel
    def get_num_crossovers_and_SUVs(self) -> int:
        return len(self.are_visible('css', self.cars_in_crossovers_and_SUVs, 'Cars in Crossovers & SUVs tab'))

    '''Cars'''

    # Return a tab for click
    def get_click_cars(self) -> WebElement:
        return self.is_visible('css', self.click_cars, 'Click Cars')

    # Return a Cars tab
    def get_category_cars(self) -> WebElement:
        return self.is_visible('css', self.button_cars, 'Count Cars')

    # Method for getting the text of Cars tab
    def get_category_cars_text(self):
        return self.get_category_cars().text

    # Return number of cars displayed on Cars grid pannel
    def get_num_cars(self) -> int:
        return len(self.are_visible('css', self.cars_in_cars, 'Cars in Cars tab'))

    '''Electric'''

    # Return a tab for click
    def get_click_electric(self):
        return self.is_visible('css', self.click_electic, 'Click Electric')

    # Return a Electric tab
    def get_category_electric(self) -> WebElement:
        return self.is_visible('css', self.button_electric, 'Electric')

    # Method for getting the text of Electric tab
    def get_category_electric_text(self):
        return self.get_category_electric().text

    # Return number of cars displayed on Electric grid pannel
    def get_num_electric(self) -> int:
        return len(self.are_visible('css', self.cars_in_electric, 'Cars in Electric tab'))

    '''Sports Cars'''

    # Return a tab for click
    def get_click_sports_cars(self):
        return self.is_visible('css', self.click_sports_cars, 'Click Sports Cars')

    # Return a Sports Cars tab
    def get_category_sports_cars(self) -> WebElement:
        return self.is_visible('css', self.button_sports_cars, 'Sports Cars')

    # Method for getting the text of Sports Cars tab
    def get_category_sports_cars_text(self):
        return self.get_category_sports_cars().text

    # Return number of cars displayed on Sports Cars grid pannel
    def get_num_sports_cars(self) -> int:
        return len(self.are_visible('css', self.cars_in_sports_cars, 'Cars in Sports Cars tab'))

    '''Trucks'''

    # Return a tab for click
    def get_click_trucks(self):
        return self.is_visible('css', self.click_trucks, 'Click Trucks')

    # Return a Trucks tab
    def get_category_trucks(self) -> WebElement:
        return self.is_visible('css', self.button_trucks, 'Trucks')

    # Method for getting the text of Trucks tab
    def get_category_trucks_text(self):
        return self.get_category_trucks().text

    # Return number of cars displayed on Trucks grid pannel
    def get_num_trucks(self) -> int:
        return len(self.are_visible('css', self.cars_in_trucks, 'Cars in Trucks tab'))
