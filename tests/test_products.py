from pages.home_page import HomePage
from pages.all_products_page import ProductsPage
from pages.single_product_page import Product
from playwright.sync_api import expect

def test_all_products_to_be_visible(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_products_page()

    products_page = ProductsPage(page)
    products_page.check_product_list_to_be_visible()    
    products_page.view_a_product(1)

    single_product_page = Product(page)
    single_product_page.check_product_details_to_be_visible()

def test_search_a_product(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_products_page()

    products_page = ProductsPage(page)
    products_page.search_a_product("men")

def test_category(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_products_page()
    
    products_page = ProductsPage(page)
    products_page.category_panel_to_be_visible()
    products_page.expand_category("Women")
    products_page.click_subcategory("Women", "Dress")
    products_page.expand_category("Men")
    products_page.click_subcategory("Men", "Jeans")


