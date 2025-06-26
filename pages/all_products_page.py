from playwright.sync_api import Page, expect

class ProductsPage:
    def __init__(self, page: Page):
        self.page=page
        self.product_list = page.locator(".features_items .product-image-wrapper")
        self.search_input = page.get_by_placeholder("Search Product")
        self.search_button =  page.locator("//button[@id='submit_search']")
        self.searched_products = page.get_by_role("heading", name = "Searched Products")
        self.continue_shopping_button = page.locator('//*[@id="cartModal"]/div/div/div[3]/button')
        self.view_cart_button = page.locator('//*[@id="cartModal"]/div/div/div[2]/p[2]/a')
        self.category_panel = page.locator('#accordian')
        self.brend_panel = page.locator("css=div.brands-name")
        self.women_category = page.get_by_role("link", name=" Women")
        self.men_categoty = page.get_by_role("link", name=" Men")
        

    def check_product_list_to_be_visible(self):
        expect(self.product_list).not_to_have_count(0)
        
    def view_a_product(self, product_index):
        self.product_list.nth(product_index-1).get_by_text("View Product").click()
        expect(self.page).to_have_url(f"https://automationexercise.com/product_details/{product_index}")

    def get_product_price(self, product_index):
        return self.product_list.nth(product_index-1).locator(".productinfo h2").text_content()
    

    def search_a_product(self, product_name):
        self.search_input.fill(product_name)
        self.search_button.click()
        expect(self.page).to_have_url(f"https://automationexercise.com/products?search={product_name}")
        expect(self.searched_products).to_be_visible()
        expect(self.product_list.nth(0)).to_be_visible()

    def add_product_to_cart(self, product_index):
        self.product_list.nth(product_index-1).locator(".productinfo .add-to-cart").click()
        expect(self.continue_shopping_button).to_be_visible()

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def view_cart(self):
        self.view_cart_button.click()

    def category_panel_to_be_visible(self):
        expect(self.category_panel).to_be_visible()

    def brend_panel_to_be_visible(self):
        expect(self.brend_panel).to_be_visible()

    def expand_category(self, category):
        if category == "Women":
            self.women_category.click()
            expect(self.page.locator('#Women > div')).to_be_visible()
        elif category == "Men":
            self.men_categoty.click()
            expect(self.page.locator('#Men > div')).to_be_visible()


    def click_subcategory(self, category, subcategory):
        self.page.get_by_role('link', name = f"{subcategory}").click()
        expect(self.page.get_by_text(f"{category} - {subcategory} Products")).to_be_visible()
        
    def click_brand(self, brand):
        self.page.get_by_role("link", name = f"{brand}").click()
        expect(self.page.get_by_text(f"Brand - {brand} Products")).to_be_visible()