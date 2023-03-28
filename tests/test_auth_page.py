# import webbrowser
# import pytest
import pytest

import time
from pages.auth_page import AuthPage

# #Тестирование формы "Авторизация"
# def test_auth_page_elements(selenium):
#     page = AuthPage(selenium)
#     assert page.get_phone_element().is_displayed() == True
#     assert page.get_mail_element().is_displayed() == True
#     assert page.get_login_element().is_displayed() == True
#     assert page.get_ls_element().is_displayed() == True
#     assert page.get_login_field().is_displayed() == True
#     assert page.get_passw_field().is_displayed() == True
#     assert page.get_logo_element().is_displayed() == True
#     assert page.get_info_element().is_displayed() == True
#     assert page.get_fogot_passw_element().is_displayed() == True
#     assert page.get_btn_element().is_displayed() == True

# #Позитивная регистрация
# @pytest.mark.parametrize('x', ["9959967398", "regpostt@mail.ru"], ids=["valid_phone", "valid_mail"])
# def test_positive_auth(selenium, x):
#    page = AuthPage(selenium)
#    page.enter_email(x)
#    page.enter_pass("Skillfactory1007")
#    page.btn_click()
#    assert page.get_relative_link() == '/account_b2c/page'

# #Негативная регистрация с неверным паролем
# @pytest.mark.parametrize('x', ["9959967398", "regpostt@mail.ru"], ids=["valid_phone", "valid_mail"])
# def test_negative_auth_wrong_passw(selenium, x):
#     page = AuthPage(selenium)
#     page.enter_email(x)
#     page.enter_pass("Skillfactory1008")
#     page.btn_click()
#     time.sleep(1)
#     assert page.get_error_massage() == "Неверный логин или пароль"


# #Негативная регистрация с неверным логином
# @pytest.mark.parametrize('x', ["9959967399", "regpost@mail.ru"], ids=["invalid_phone", "invalid_mail"])
# def test_negative_auth_wrong_passw(selenium, x):
#     page = AuthPage(selenium)
#     page.enter_email(x)
#     page.enter_pass("Skillfactory1007")
#     page.btn_click()
#     time.sleep(1)
#     assert page.get_error_massage() == "Неверный логин или пароль"

# # По умолчанию выбрана форма авторизации по телефону
# def test_registration_page_elements(selenium):
#    page  = AuthPage(selenium)
#    assert page.get_phone_element().get_attribute("class") == "rt-tab rt-tab--small rt-tab--active"
#    assert page.get_phone_element().text == 'Телефон'
#    assert page.get_mail_element().get_attribute("class") != "rt-tab rt-tab--small rt-tab--active"

# def test_registration(selenium):
#    page = AuthPage(selenium)
#    page.reg_click()
#    assert page.get_relative_link() == '/account_b2c/page'