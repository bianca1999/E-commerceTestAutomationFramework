from pages.home_page import HomePage
from pages.all_products_page import ProductsPage
from pages.cart_page import CartPage

def test_add_products_to_cart(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_products_page()

    products_page = ProductsPage(page)
    products_page.add_product_to_cart(1)
    product1_price = products_page.get_product_price(1)

    products_page.continue_shopping()

    products_page.add_product_to_cart(2)
    product2_price = products_page.get_product_price(2)
    products_page.view_cart()
    
    cart_page = CartPage(page)
    cart_page.test_if_a_product_is_in_the_cart(1, product1_price, "1", product1_price)
    cart_page.test_if_a_product_is_in_the_cart(2, product2_price, "1", product2_price)

