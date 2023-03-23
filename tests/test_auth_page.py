from pages.auth_page import AuthPage


def test_mail_auth_page(selenium):
   page = AuthPage(selenium)
   page.enter_email("regpostt@mail.ru")
   page.enter_pass("Skillfactory1007")
   page.btn_click()
   assert page.get_relative_link() == '/account_b2c/page'


def test_phone_auth_page(selenium):
   page = AuthPage(selenium)
   page.enter_phone("9959967398")
   page.enter_pass("Skillfactory1007")
   page.btn_click()
   assert page.get_relative_link() == '/account_b2c/page'

def test_phone_auth_page_negative(selenium):
   page = AuthPage(selenium)
   page.enter_phone("9959967398")
   page.enter_pass("Skillfactory1008")
   page.btn_click()
   assert page.get_relative_link() == '/account_b2c/page'