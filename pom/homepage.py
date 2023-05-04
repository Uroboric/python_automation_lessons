from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import SeleniumBase
from typing import List


class HomepageNav(SeleniumBase):
    # CSS locators
    link_crossovers_and_suvs = '.c_310_tertiary_grid_slider [data-label="Crossovers & SUVs"]'
    button_crossovers_and_suvs = '.c_310_tertiary_grid_slider button[data-bodystyle="Crossovers & SUVs"] .c_310-vehicles-count'
    cars_in_crossovers_and_suvs = '#vehiclelist--1738608765_categoryPanel_0 .c_310-1'

    link_cars = '.c_310_tertiary_grid_slider [data-label="Cars"]'
    button_cars = '.c_310_tertiary_grid_slider button[data-bodystyle="Cars"] .c_310-vehicles-count'
    cars_in_cars = '#vehiclelist--1738608765_categoryPanel_1 .c_310-1'

    link_electric = '.c_310_tertiary_grid_slider button[data-bodystyle="Electric"]'
    button_electric = '.c_310_tertiary_grid_slider button[data-bodystyle="Electric"] .c_310-vehicles-count'
    cars_in_electric = '#vehiclelist--1738608765_categoryPanel_2 .c_310-1'

    link_sports_cars = '.c_310_tertiary_grid_slider button[data-bodystyle="Sports Cars"]'
    button_sports_cars = '.c_310_tertiary_grid_slider button[data-bodystyle="Sports Cars"] .c_310-vehicles-count'
    cars_in_sports_cars = '#vehiclelist--1738608765_categoryPanel_3 .c_310-1'

    link_trucks = '.c_310_tertiary_grid_slider button[data-bodystyle="Trucks"]'
    button_trucks = '.c_310_tertiary_grid_slider button[data-bodystyle="Trucks"] .c_310-vehicles-count'
    cars_in_trucks = '#vehiclelist--1738608765_categoryPanel_4 .c_310-1'

    '''Crossovers & SUVs'''

    # Return a tab for click
    def get_crossovers_and_suvs_link(self) -> WebElement:
        return self.is_visible('css', self.link_crossovers_and_suvs, 'Grid slider link - Cars')

    # Return a Crossovers & SUVs count tab
    def get_category_crossovers_and_suvs(self) -> WebElement:
        return self.is_visible('css', self.button_crossovers_and_suvs, 'Grid slider link - Crossovers & SUVs')

    # Method for getting the text of Crossovers & SUVs count tab
    def get_category_crossovers_and_suvs_text(self) -> str:
        return self.get_category_crossovers_and_suvs().text

    # Return number of cars displayed on Crossovers & SUVs grid panel
    def get_tab_catgory_crossovers_and_suvs(self) -> List[WebElement]:
        return self.are_visible('css', self.cars_in_crossovers_and_suvs, 'Cars in Crossovers & SUVs category panel')

    # Return number of cars displayed on Crossovers & SUVs category panel
    def get_num_crossovers_and_suvs(self) -> int:
        return len(self.get_tab_catgory_crossovers_and_suvs())

    '''Cars'''

    # Return a tab for click
    def get_cars_link(self) -> WebElement:
        return self.is_visible('css', self.link_cars, 'Grid slider link - Cars')

    # Return a Cars count tab
    def get_category_cars(self) -> WebElement:
        return self.is_visible('css', self.button_cars, 'Count tab - Cars')

    # Method for getting the text of Cars count tab
    def get_category_cars_text(self) -> str:
        return self.get_category_cars().text

    # Return a list of web elements in category panel
    def get_tab_category_cars(self) -> List[WebElement]:
        return self.are_visible('css', self.cars_in_cars, 'Cars in Cars category panel')

    # Return number of cars displayed on Cars category panel
    def get_num_cars(self) -> int:
        return len(self.get_tab_category_cars())

    '''Electric'''

    # Return a tab for click
    def get_electric_link(self):
        return self.is_visible('css', self.link_electric, 'Grid slider link - Electric')

    # Return a Electric count tab
    def get_category_electric(self) -> WebElement:
        return self.is_visible('css', self.button_electric, 'Count tab - Electric')

    # Method for getting the text of Electric count tab
    def get_category_electric_text(self) -> str:
        return self.get_category_electric().text

    # Return number of cars displayed on Electric category panel
    def get_tab_category_electric(self) -> List[WebElement]:
        return self.are_visible('css', self.cars_in_electric, 'Cars in Electric category panel')

    # Return number of cars displayed on Electric category panel
    def get_num_electric(self) -> int:
        return len(self.get_tab_category_electric())

    '''Sports Cars'''

    # Return a tab for click
    def get_sports_cars_link(self):
        return self.is_visible('css', self.link_sports_cars, 'Grid slider link - Sports Cars')

    # Return a Sports Cars count tab
    def get_category_sports_cars(self) -> WebElement:
        return self.is_visible('css', self.button_sports_cars, 'Count tab - Sports Cars')

    # Method for getting the text of Sports Cars count tab
    def get_category_sports_cars_text(self) -> str:
        return self.get_category_sports_cars().text

    # Return number of cars displayed on Sports Cars category panel
    def get_tab_category_sports_cars(self) -> List[WebElement]:
        return self.are_visible('css', self.cars_in_sports_cars, 'Cars in Sports Cars category panel')

    # Return number of cars displayed on Sports Cars category panel
    def get_num_sports_cars(self) -> int:
        return len(self.get_tab_category_sports_cars())

    '''Trucks'''

    # Return a tab for click
    def get_trucks_link(self):
        return self.is_visible('css', self.link_trucks, 'Grid slider link - Trucks')

    # Return a Trucks count tab
    def get_category_trucks(self) -> WebElement:
        return self.is_visible('css', self.button_trucks, 'Count tab - Trucks')

    # Method for getting the text of Trucks count tab
    def get_category_trucks_text(self) -> str:
        return self.get_category_trucks().text

    # Return number of cars displayed on Trucks category panel
    def get_tab_category_trucks(self) -> List[WebElement]:
        return self.are_visible('css', self.cars_in_trucks, 'Cars in Trucks category panel')

    # Return number of cars displayed on Trucks category panel
    def get_num_trucks(self) -> int:
        return len(self.get_tab_category_trucks())
