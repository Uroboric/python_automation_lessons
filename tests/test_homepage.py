import pytest
from pom.homepage import Homepage


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_homepage_text(self):
        homepage = Homepage(self.driver)
        assert homepage.get_vehicles_text() == "Vehicles"
        assert homepage.get_shop_at_home_text() == "Shop At Home"
        assert homepage.get_discover_nissan_text() == "Discover Nissan"
        assert homepage.get_owners_text() == "Owners"
        assert homepage.get_locate_dealer_text() == "Locate Dealer"
        assert homepage.get_build_and_price_text() == "Build & Price"