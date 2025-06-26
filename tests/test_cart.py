from pages.home_page import HomePage
from pages.all_products_page import ProductsPage
from pages.cart_page import CartPage
from pages.single_product_page import Product
import pytest

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

@pytest.mark.parametrize('product_id', [1, 2, 3, 4])
def test_verify_product_quantity_in_cart(page, product_id):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_products_page()

    products_page = ProductsPage(page)
    products_page.view_a_product(product_id)

    single_product_page = Product(page)
    single_product_page.check_product_details_to_be_visible()
    single_product_page.update_quantity("4")
    total_price = single_product_page.get_the_total_price_based_on_quantity("4")
    single_product_page.add_to_cart()

    single_product_page.view_cart()

    cart_page = CartPage(page)
    cart_page.test_total_price_for_a_product(product_id, total_price)

def test_remove_product_from_cart(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_products_page()

    products_page = ProductsPage(page)
    products_page.add_product_to_cart(1)
    products_page.continue_shopping()
    products_page.add_product_to_cart(2)
    products_page.view_cart()

    cart_page = CartPage(page)
    cart_page.remove_a_product_from_the_cart(1)
    
