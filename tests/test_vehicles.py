import allure
import pytest
from pom.vehicles import VehiclesNav


@allure.suite("Testing Vehicles parametrize")
@pytest.mark.usefixtures('setup')
@pytest.mark.parallel
class TestVehicles:
    test_data = [('Ariya', '$39,590'), ('Kicks', '$21,340'), ('Rogue Sport', '$24,960'), ('Rogue', '$28,850'),
                 ('Murano', '$38,740'), ('Pathfinder', '$36,650'), ('Armada', '$56,520')]

    @allure.title("Asserting Vehicles prices")
    @pytest.mark.parametrize('car_name, expected_price', test_data)
    def test_vehicle_price(self, car_name, expected_price):
        vehicles = VehiclesNav(self.driver)
        vehicles.get_button_to_be_clickable().click()
        # print(f"Current URL: {self.driver.current_url}")
        # vehicles.get_button_vehicles_present().click()
        # print(f"Current URL: {self.driver.current_url}")
        vehicles.get_button_vehicles_visible().click()
        vehicles.get_car_link(car_name).click()
        actual_price = vehicles.get_car_price_text(car_name)
        assert actual_price == expected_price
