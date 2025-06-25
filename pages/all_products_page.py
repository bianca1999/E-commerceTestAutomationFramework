from playwright.sync_api import Page, expect

class ProductsPage:
    def __init__(self, page: Page):
        self.page=page
        self.product_list = page.locator(".features_items .product-image-wrapper")
        self.search_input = page.get_by_placeholder("Search Product")
        self.search_button =  page.locator("//button[@id='submit_search']")
        
        self.searched_products = page.get_by_role("heading", name = "Searched Products")
        
        

    def check_product_list_to_be_visible(self):
        expect(self.product_list).not_to_have_count(0)
        
    def view_a_product(self, product_index):
        self.product_list.nth(product_index-1).get_by_text("View Product").click()
        expect(self.page).to_have_url(f"https://automationexercise.com/product_details/{product_index}")

    def search_a_product(self, product_name):
        self.search_input.fill(product_name)
        self.search_button.click()
        expect(self.page).to_have_url(f"https://automationexercise.com/products?search={product_name}")
        expect(self.searched_products).to_be_visible()
        expect(self.product_list.nth(0)).to_be_visible()
