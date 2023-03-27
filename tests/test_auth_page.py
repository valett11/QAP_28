import webbrowser

import pytest

from pages.auth_page import AuthPage

#
# def test_mail_auth_page(selenium):
#    page = AuthPage(selenium)
#    page.enter_email("regpostt@mail.ru")
#    page.enter_pass("Skillfactory1007")
#    page.btn_click()
#    assert page.get_relative_link() == '/account_b2c/page'


# def test_phone_auth_page(selenium):
#    page = AuthPage(selenium)
#    page.enter_phone("9959967398")
#    page.enter_pass("Skillfactory1007")
#    page.btn_click()
#    assert page.get_relative_link() == '/account_b2c/page'
#
# def test_phone_auth_page_negative(selenium):
#    page = AuthPage(selenium)
#    page.enter_phone("9959967398")
#    page.enter_pass(input('Skillfactory1008'))
#    page.btn_click()
#    assert page.get_relative_link() == '/account_b2c/page'
#
# def test_registration(selenium):
#    page = AuthPage(selenium)
#    page.reg_click()
#
#    assert page.get_relative_link() == '/account_b2c/page'

# def test_registration_page_elements(selenium):
#    page  = AuthPage(selenium)
#    a = page.get_phone_element()
#    assert a.get_attribute("class") == "rt-tab rt-tab--small rt-tab--active"
#    assert  a.text == 'Телефон'
#    assert a.is_displayed() == True

# @pytest.mark.parametrize('x', ["regpostt@mail.ru", "regpstt@mail.ru", "regposttmail.ru"], ids=["positive", "negative", "negative2"])
# def test_mail_auth_page(selenium, x):
#    page = AuthPage(selenium)
#    page.enter_email(x)
#    page.enter_pass("Skillfactory1007")
#    page.btn_click()
#    assert page.get_relative_link() == '/account_b2c/page'