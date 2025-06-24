from pages.home_page import HomePage
from pages.contact_us_page import ContactUsPage

def test_test_cases_page(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_test_cases_page()