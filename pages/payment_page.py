from playwright.sync_api import Page, expect

class PaymentPage:
    def __init__(self,page:Page):
        self.page = page


    def fill_payment_details(self, name_on_card, card_number, CVC, expiry_month, expiry_year):
        self.page.locator('input[name="name_on_card"]').fill(name_on_card)
        self.page.locator('input[name="card_number"]').fill(card_number)
        self.page.locator('input[name="cvc"]').fill(CVC)
        self.page.locator('input[name="expiry_month"]').fill(expiry_month)
        self.page.locator('input[name="expiry_year"]').fill(expiry_year)

    def pay_and_confirm_order(self):
        self.page.get_by_role('button',name='Pay and Confirm Order').click()
        expect(self.page.get_by_text('Order Placed!')).to_be_visible()
