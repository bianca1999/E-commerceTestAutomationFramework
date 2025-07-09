from pages.home_page import HomePage
from pages.payment_page import PaymentPage
import pytest
import json

with open('./data/correct_login_credentials.json') as f:
    correct_credentials_data = json.load(f)
    correct_credentials_list = correct_credentials_data['correct_login_credentials']

with open('./data/payment_details.json') as f:
    payment_data = json.load(f)
    payment_list = payment_data['payment_details']

@pytest.mark.parametrize(["credentials", "payment_details"], list(zip(correct_credentials_list, payment_list)))
def test_place_order_with_login_while_checkout(page, credentials, payment_details):
    home_page = HomePage(page)
    home_page.navigate()

    products_page = home_page.go_to_products_page()
    products_page.add_product_to_cart(1)
    products_page.continue_shopping()
    products_page.add_product_to_cart(2)

    cart_page = products_page.view_cart()
    cart_page.proceed_to_checkout()

    login_page = cart_page.register_or_login_while_checkout()
    login_page.user_login(credentials['userEmail'],credentials['userPassword'])
    login_page.expect_login_success()

    home_page.go_to_cart_page()
    cart_page.proceed_to_checkout()
    cart_page.check_if_address_details_are_visible()
    cart_page.check_if_review_your_order_section_is_visible()
    cart_page.fill_message_area("This is my message!")
    cart_page.place_order()

    payment_page = PaymentPage(page)
    payment_page.fill_payment_details(payment_details["name_on_card"],
                                      payment_details["card_number"],
                                      payment_details["cvc"],
                                      payment_details["exp_month"],
                                      payment_details["exp_year"])
    payment_page.pay_and_confirm_order()


    

