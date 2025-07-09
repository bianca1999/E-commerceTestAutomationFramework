from pages.home_page import HomePage
import os
import json
import pytest

with open('./data/contact_us_form_details.json') as ilc:
    contact_us_form_data = json.load(ilc)
    contact_us_form_list = contact_us_form_data['contact_us_form_details']

@pytest.mark.parametrize('credentials', contact_us_form_list)
def test_contact_us_test(page, credentials):
    home_page = HomePage(page)
    home_page.navigate()

    contact_us_page = home_page.go_to_contact_us_page()
    file_path = os.path.abspath("files/my_file.txt")
    contact_us_page.fill_contact_form(credentials['name'],
                                      credentials['email'],
                                      credentials['subject'],
                                      credentials['message']
                                      )
