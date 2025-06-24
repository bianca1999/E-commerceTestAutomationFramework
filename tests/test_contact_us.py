from pages.home_page import HomePage
from pages.contact_us_page import ContactUsPage
import os

def test_contact_us_test(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_contact_us_page()

    contact_us_page = ContactUsPage(page)
    file_path = os.path.abspath("files/my_file.txt")
    contact_us_page.fill_contact_form("Bianca",
                                      "bianca@gmail.com",
                                      "subject",
                                      "message"
                                      )
