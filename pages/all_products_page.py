from playwright.sync_api import Page, expect
from pages.cart_page import CartPage
from pages.single_product_page import Product


class ProductsPage:
    def __init__(self, page: Page):
        self.page=page


    def check_product_list_to_be_visible(self):
        expect(self.page.locator(".features_items .product-image-wrapper")).not_to_have_count(0)


    def view_a_product(self, product_index):
        self.page.locator(".features_items .product-image-wrapper").nth(product_index-1).get_by_text("View Product").click()
        expect(self.page).to_have_url(f"https://automationexercise.com/product_details/{product_index}")
        product = Product(self.page)
        return product


    def get_product_price(self, product_index):
        return self.page.locator(".features_items .product-image-wrapper").nth(product_index-1).locator(".productinfo h2").text_content()


    def search_a_product(self, product_name):
        self.page.get_by_placeholder("Search Product").fill(product_name)
        self.page.locator("#submit_search").click()
        expect(self.page).to_have_url(f"https://automationexercise.com/products?search={product_name}")
        expect(self.page.get_by_role("heading", name = "Searched Products")).to_be_visible()


    def add_product_to_cart(self, product_index):
        self.page.locator(".features_items .product-image-wrapper").nth(product_index-1).locator(".productinfo .add-to-cart").click()
        expect(self.page.get_by_role("button", name="Continue Shopping")).to_be_visible()


    def continue_shopping(self):
        self.page.get_by_role("button", name="Continue Shopping").click()


    def view_cart(self):
        self.page.get_by_role("link", name = "View Cart").click()

        cartPage = CartPage(self.page)
        return cartPage


    def category_panel_to_be_visible(self):
        expect(self.page.locator('#accordian')).to_be_visible()


    def brand_panel_to_be_visible(self):
        expect(self.page.locator(".brands-name")).to_be_visible()


    def expand_category(self, category):
        if category == "Women":
            self.page.get_by_role("link", name="Women").click()
            expect(self.page.locator('#Women > div')).to_be_visible()
        elif category == "Men":
            self.page.get_by_role("link", name=" Men ", exact=True).click()
            expect(self.page.locator('#Men > div')).to_be_visible()


    def click_subcategory(self, category, subcategory):
        self.page.get_by_role('link', name = f"{subcategory}").click()
        expect(self.page.get_by_text(f"{category} - {subcategory} Products")).to_be_visible()


    def click_brand(self, brand):
        self.page.get_by_role("link", name = f"{brand}").click()
        expect(self.page.get_by_text(f"Brand - {brand} Products")).to_be_visible()