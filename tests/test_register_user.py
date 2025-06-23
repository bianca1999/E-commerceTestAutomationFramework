from pages.home_page import HomePage

def test_register_user(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_signup_login_page()