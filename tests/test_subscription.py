from pages.home_page import HomePage
from pages.cart_page import CartPage

def test_subscription_in_home_page(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.verify_subscription("calancea.bianca15@gmail.com")

def test_subscription_in_cart_page(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_cart_page()

    cart_page = CartPage(page)
    cart_page.verify_subscription("calancea.bianca15@gmail.com")