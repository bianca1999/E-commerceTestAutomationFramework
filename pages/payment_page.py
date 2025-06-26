from playwright.sync_api import Page, expect

class PaymentPage:
    def __init__(self,page:Page):
        self.page = page
        self.name_on_card = page.locator('input[name="name_on_card"]')
        self.card_number = page.locator('input[name="card_number"]')
        self.CVC = page.locator('input[name="cvc"]')
        self.expiry_month = page.locator(('input[name="expiry_month"]'))
        self.expiry_year = page.locator(('input[name="expiry_year"]'))
        self.pay_and_confirm_order_button = page.get_by_text('Pay and Confirm Order')
        self.order_placed_message = page.get_by_text('Order Placed!')


    def fill_payment_details(self, name_on_card, card_number, CVC, expiry_month, expiry_year):
        self.name_on_card.fill(name_on_card)
        self.card_number.fill(card_number)
        self.CVC.fill(CVC)
        self.expiry_month.fill(expiry_month)
        self.expiry_year.fill(expiry_year)

    def pay_and_confirm_order(self):
        self.pay_and_confirm_order_button.click()
        expect(self.order_placed_message).to_be_visible()
