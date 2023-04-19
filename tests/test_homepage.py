import pytest
from pom.homepage import HomepageNav
from pytest_check import check


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_homepage_tabs(self):
        # crossovers_and_SUVs
        homepage = HomepageNav(self.driver)
        num_tab_crossovers_and_SUVs = int(homepage.get_category_crossovers_and_SUVs_text())
        num_grid_pannel_crossovers_and_SUVs = homepage.get_num_crossovers_and_SUVs()
        check.equal(num_tab_crossovers_and_SUVs, num_grid_pannel_crossovers_and_SUVs)

        # Cars
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", homepage.get_click_cars())
        homepage.get_click_cars().click()
        num_tab_cars = int(homepage.get_category_cars_text())
        num_grid_pannel_cars = homepage.get_num_cars()
        check.equal(num_tab_cars, num_grid_pannel_cars)

        # Electric
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", homepage.get_click_electric())
        homepage.get_click_electric().click()
        num_tab_electric = int(homepage.get_category_electric_text())
        num_grid_pannel_electric = homepage.get_num_electric()
        check.equal(num_tab_electric, num_grid_pannel_electric)

        # Sports cars
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", homepage.get_click_sports_cars())
        homepage.get_click_sports_cars().click()
        num_tab_sports_cars = int(homepage.get_category_sports_cars_text())
        num_grid_pannel_sports_cars = homepage.get_num_sports_cars()
        check.equal(num_tab_sports_cars, num_grid_pannel_sports_cars)

        # Trucks
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", homepage.get_click_trucks())
        homepage.get_click_trucks().click()
        num_tab_trucks = int(homepage.get_category_trucks_text())
        num_grid_pannel_trucks = homepage.get_num_trucks()
        check.equal(num_tab_trucks, num_grid_pannel_trucks)
