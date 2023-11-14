import allure
import pytest
from pom.vehicles import VehiclesNav


@allure.suite("Testing Vehicles parametrize")
@pytest.mark.usefixtures('setup')
@pytest.mark.parallel
class TestVehicles:
    test_data = [('Ariya', '$43,190'), ('Kicks', '$20,440'), ('Rogue Sport', '$24,960'), ('Rogue', '$27,910'),
                 ('Murano', '$34,160'), ('Pathfinder', '$35,320'), ('Armada', '$50,700')]

    @allure.title("Asserting Vehicles prices")
    @pytest.mark.parametrize('car_name, expected_price', test_data)
    def test_vehicle_price(self, car_name, expected_price):
        vehicles = VehiclesNav(self.driver)
        vehicles.get_button_vehicles().click()
        vehicles.get_car_link(car_name).click()
        actual_price = vehicles.get_car_price_text(car_name)
        assert actual_price == expected_price
