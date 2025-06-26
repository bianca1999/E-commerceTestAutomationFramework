from playwright.sync_api import Page, expect

class Product:
    def __init__(self, page:Page):
        self.page = page
        self.product_name = page.locator("div.product-information h2")
        self.product_category = page.get_by_text("Category:")
        self.product_price = page.get_by_text("Rs.")
        self.product_availability = page.get_by_text("Availability:")
        self.product_condition = page.get_by_text("Condition:")
        self.product_brand = page.get_by_text("Brand:")
        self.product_quantity = page.locator('//*[@id="quantity"]')
        self.add_to_cart_button = page.get_by_text('Add to cart')
        self.continue_shopping_button = page.locator('//*[@id="cartModal"]/div/div/div[3]/button')
        self.view_cart_button = page.locator('//*[@id="cartModal"]/div/div/div[2]/p[2]/a')

    def check_product_details_to_be_visible(self):
        expect(self.product_name).to_be_visible()
        expect(self.product_category).to_be_visible()
        expect(self.product_price).to_be_visible()
        expect(self.product_availability).to_be_visible()
        expect(self.product_condition).to_be_visible()
        expect(self.product_brand).to_be_visible()

    def update_quantity(self, quantity_value):
        self.product_quantity.clear()
        self.product_quantity.fill(quantity_value)

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def view_cart(self):
        self.view_cart_button.click()

    def get_the_total_price_based_on_quantity(self, product_quantity):
        price = self.product_price.text_content()[4:]
        total_price = int(price) * int(product_quantity)
        return f"Rs. {total_price}"
        

