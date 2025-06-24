from pages.login_page import LoginPage

def test_login_user_correct_credentials(page, go_to_signup_login):
    go_to_signup_login()

    login_page = LoginPage(page)
    login_page.user_login_correct_credentials("bianca@gmail",
                                   "123456")
    


def test_login_user_incorrect_credentials(page, go_to_signup_login):
    go_to_signup_login()

    login_page = LoginPage(page)
    login_page.user_login_incorrect_credentials("bianca@gmail",
                                   "123")


