from pages.home_page import HomePage
from pages.all_products_page import ProductsPage
from pages.single_product_page import Product
import pytest

@pytest.mark.parametrize('product_id', [1, 2, 3, 4])
def test_products_to_be_visible(page, product_id):
    home_page = HomePage(page)
    home_page.navigate()
    products_page = home_page.go_to_products_page()
    products_page.check_product_list_to_be_visible()
    single_product_page = products_page.view_a_product(product_id)
    single_product_page.check_product_details_to_be_visible()


@pytest.mark.parametrize('product_name', ["men",
                                          "women", 
                                          "kids"])
def test_search_a_product(page, product_name):
    home_page = HomePage(page)
    home_page.navigate()
    products_page = home_page.go_to_products_page()
    products_page.search_a_product(product_name)

@pytest.mark.parametrize('category, subcategory', [["Women", "Dress"], 
                                                   ["Women", "Tops"],
                                                   ["Women", "Saree"]
                                                   ])
def test_category(page, category, subcategory):
    home_page = HomePage(page)
    home_page.navigate()
    products_page = home_page.go_to_products_page()
    products_page.category_panel_to_be_visible()
    products_page.expand_category(category)
    products_page.click_subcategory(category, subcategory)

@pytest.mark.parametrize('brand', ["POLO",
                                    "H&M", 
                                    "MADAME", 
                                    "BABYHUG", 
                                    "MAST & HARBOUR", 
                                    "BIBA", 
                                    "KOOKIE KIDS"])
def test_brand(page, brand):
    home_page = HomePage(page)
    home_page.navigate()
    products_page = home_page.go_to_products_page()
    products_page.brand_panel_to_be_visible()
    products_page.click_brand(brand)