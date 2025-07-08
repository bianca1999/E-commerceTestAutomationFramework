from playwright.sync_api import Page, expect

from pages.cart_page import CartPage


class Product:
    def __init__(self, page:Page):
        self.page = page


    def check_product_details_to_be_visible(self):
        expect(self.page.locator(".product-information h2")).to_be_visible()
        expect(self.page.get_by_text("Category:")).to_be_visible()
        expect(self.page.get_by_text("Rs.")).to_be_visible()
        expect(self.page.get_by_text("Availability:")).to_be_visible()
        expect(self.page.get_by_text("Condition:")).to_be_visible()
        expect(self.page.get_by_text("Brand:")).to_be_visible()

    def update_quantity(self, quantity_value):
        self.page.locator('#quantity').clear()
        self.page.locator('#quantity').fill(quantity_value)

    def add_to_cart(self):
        self.page.get_by_text('Add to cart').click()

    def continue_shopping(self):
        self.page.get_by_role("button",name="Continue Shopping").click()

    def view_cart(self):
        self.page.get_by_role("link", name = "View Cart").click()

        cart = CartPage(self.page)
        return cart

    def get_the_total_price_based_on_quantity(self, product_quantity):
        price = self.page.get_by_text("Rs.").text_content()[4:]
        total_price = int(price) * int(product_quantity)
        return f"Rs. {total_price}"
        

