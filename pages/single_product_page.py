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

    def check_product_details_to_be_visible(self):
        expect(self.product_name).to_be_visible()
        expect(self.product_category).to_be_visible()
        expect(self.product_price).to_be_visible()
        expect(self.product_availability).to_be_visible()
        expect(self.product_condition).to_be_visible()
        expect(self.product_brand).to_be_visible()

