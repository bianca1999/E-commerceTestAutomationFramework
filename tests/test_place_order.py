from pages.home_page import HomePage
from pages.all_products_page import ProductsPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.payment_page import PaymentPage

def test_place_order_with_register_while_checkout(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_products_page()

    products_page = ProductsPage(page)
    products_page.add_product_to_cart(1)
    products_page.continue_shopping()
    products_page.add_product_to_cart(2)
    products_page.view_cart()

    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()
    cart_page.register_or_login_while_checkout()

    login_page = LoginPage(page)
    login_page.user_login_correct_credentials("bianca@gmail",'123456')

    home_page.go_to_cart_page()
    cart_page.proceed_to_checkout()
    cart_page.check_if_address_details_are_visible()
    cart_page.check_if_review_your_order_section_is_visible()
    cart_page.fill_message_area("This is my message!")
    cart_page.place_order()

    payment_page = PaymentPage(page)
    payment_page.fill_payment_details("Bianca calancea",
                                      "123456789",
                                      "123",
                                      "12",
                                      "2028")
    payment_page.pay_and_confirm_order()


    

