import pytest
from pom.homepage import HomepageNav

expected_nav_links_value = ['Vehicles', 'Shop At Home', 'Discover Nissan', 'Owners', 'Locate Dealer']
expected_build_price_value = 'Build & Price'


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_homepage_text(self):
        homepage = HomepageNav(self.driver)
        actual_nav_links = homepage.get_nav_links_text()
        actual_build_price = homepage.get_build_price_text()
        assert actual_nav_links == expected_nav_links_value, 'Validating Nav Links text'
        assert actual_build_price == expected_build_price_value, 'Validating Build & Price text'
