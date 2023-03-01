import pytest
from pom.homepage import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_homepage_text(self):
        homepage = HomepageNav(self.driver)
        verify_categories = 'Vehicles,Shop At Home,Discover Nissan,Owners,Locate Dealer'
        verify_category = 'Build & Price'
        actual_links = (",".join(homepage.get_nav_links_text()), homepage.get_nav_link_text())
        expected_links = (verify_categories, verify_category)
        assert actual_links == expected_links, 'Validating Nav Links text'
