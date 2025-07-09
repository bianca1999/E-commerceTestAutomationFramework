from pages.home_page import HomePage
import pytest

@pytest.mark.parametrize('email', ["calancea.bianca15@gmail.com",
                                   "calancea@gmail.com",
                                   "petru@gmai.com"
                                    ])
def test_subscription_in_home_page(page, email):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.verify_subscription(email)

@pytest.mark.parametrize('email', ["calancea.bianca15@gmail.com",
                                   "calancea@gmail.com",
                                   "petru@gmai.com"
                                    ])
def test_subscription_in_cart_page(page, email):
    home_page = HomePage(page)
    home_page.navigate()
    cart_page = home_page.go_to_cart_page()
    cart_page.verify_subscription(email)