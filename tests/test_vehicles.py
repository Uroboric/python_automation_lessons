import pytest
import time
from pom.vehicles import VehiclesNav


@pytest.mark.usefixtures('setup')
@pytest.mark.parallel
class TestVehicles:
    test_data = [('Ariya', '$43,190'), ('Kicks', '$20,440'), ('Rogue Sport', '$24,960'), ('Rogue', '$27,760'),
                 ('Murano', '$34,160'), ('Pathfinder', '$35,200'), ('Armada', '$50,700')]

    @pytest.mark.parametrize('car_name, expected_price', test_data)
    def test_vehicle_price(self, car_name, expected_price):
        vehicles = VehiclesNav(self.driver)
        time.sleep(2)
        vehicles.get_button_vehicles().click()
        vehicles.get_car_link(car_name).click()
        actual_price = vehicles.get_car_price_text(car_name)
        assert actual_price == expected_price
