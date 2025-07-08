import pytest

from pages.login_page import LoginPage
import json

#parsing json file for correct credentials
with open('./data/correct_login_credentials.json') as clc:
    correct_credentials_data = json.load(clc)
    correct_credentials_list = correct_credentials_data['correct_login_credentials']

@pytest.mark.parametrize('correct_credentials', correct_credentials_list)
def test_login_user_correct_credentials(page, correct_credentials, go_to_signup_login, logout_user):
    go_to_signup_login()
    login_page = LoginPage(page)
    login_page.user_login(correct_credentials['userEmail'], correct_credentials['userPassword'])
    login_page.expect_login_success()
    logout_user()


#parsing json file for incorrect credentials
with open('./data/incorrect_login_credentials.json') as ilc:
    incorrect_credentials_data = json.load(ilc)
    incorrect_credentials_list = incorrect_credentials_data['incorrect_login_credentials']

@pytest.mark.parametrize('incorrect_credentials', incorrect_credentials_list)
def test_login_user_incorrect_credentials(page, incorrect_credentials, go_to_signup_login):
    go_to_signup_login()

    login_page = LoginPage(page)
    login_page.user_login(incorrect_credentials["userEmail"], incorrect_credentials["userPassword"])
    login_page.expect_login_failure()


