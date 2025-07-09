from pages.login_page import LoginPage
from pages.signup_page import SignupPage
import json
import pytest

with open('./data/correct_register_details.json') as crd:
    correct_credentials_data = json.load(crd)
    correct_credentials_list = correct_credentials_data['correct_register_details']

@pytest.mark.parametrize('credentials', correct_credentials_list)
def test_user_register_correct_credentials(page, credentials, go_to_signup_login, delete_account):
    go_to_signup_login()

    login_page = LoginPage(page)
    login_page.user_register(credentials["name"], credentials["email"])
    login_page.expect_register_success()

    signup_page = SignupPage(page)
    signup_page.set_user_title(credentials["title"])
    signup_page.enter_account_information(
                                          credentials["password"],
                                          credentials["birthday"],
                                          credentials["birth_month"],
                                          credentials["birth_year"])
    signup_page.check_for_newsletter()
    signup_page.check_for_offers()

    signup_page.enter_address_information(credentials["name"],
                                          credentials["last_name"],
                                          credentials["company"],
                                          credentials["address1"],
                                          credentials["address2"],
                                          credentials["country"],
                                          credentials["state"],
                                          credentials["city"],
                                          credentials["zipcode"],
                                          credentials["phone"])
    
    signup_page.click_continue_button()
    delete_account()


with open('./data/incorrect_register_details.json') as ird:
    incorrect_credentials_data = json.load(ird)
    incorrect_credentials_list = incorrect_credentials_data['incorrect_register_details']

@pytest.mark.parametrize('credentials', incorrect_credentials_list)
def test_user_register_incorrect_credentials(page, credentials, go_to_signup_login):
    go_to_signup_login()
    login_page = LoginPage(page)
    login_page.user_register(credentials["name"], credentials["email"])
    login_page.expect_register_failure()
