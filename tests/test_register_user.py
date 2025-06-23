from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage


def test_register_user(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_signup_login_page()

    login_page = LoginPage(page)
    login_page.new_user_signup("Bianca", "calancea.bianca15@gmail.com")

    signup_page = SignupPage(page)
    signup_page.set_user_title("Mrs")
    signup_page.enter_account_information(
                                          "password",
                                          "15",
                                          "7",
                                          "1999")
    signup_page.check_for_newsletter()
    signup_page.check_for_offers()

    signup_page.enter_address_information("Bianca",
                                          "Calancea",
                                          "Continental",
                                          "Hensman Street",
                                          "Kewdale",
                                          "Australia",
                                          "WA",
                                          "Perth",
                                          "6104",
                                          "0422569234")