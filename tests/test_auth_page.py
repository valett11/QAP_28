
import pytest

import time
from pages.auth_page import AuthPage, RestorePage

#1Тестирование формы "Авторизация"
def test_auth_page_elements(selenium):
    page = AuthPage(selenium)
    assert page.get_phone_element().is_displayed() == True
    assert page.get_mail_element().is_displayed() == True
    assert page.get_login_element().is_displayed() == True
    assert page.get_ls_element().is_displayed() == True
    assert page.get_login_field().is_displayed() == True
    assert page.get_passw_field().is_displayed() == True
    assert page.get_fogot_passw_element().is_displayed() == True
    assert page.get_btn_element().is_displayed() == True

#2Позитивная авторизация
@pytest.mark.parametrize('x', ["9959967398", "regpostt@mail.ru"], ids=["valid_phone", "valid_mail"])
def test_positive_auth(selenium, x):
   page = AuthPage(selenium)
   page.enter_email(x)
   page.enter_pass("Skillfactory1007")
   page.btn_click()
   assert page.get_relative_link() == '/account_b2c/page'

#3Негативная регистрация с неверным логином
@pytest.mark.parametrize('x', ["9959967399", "regpost@mail.ru"], ids=["invalid_phone", "invalid_mail"])
def test_negative_auth_wrong_passw(selenium, x):
    page = AuthPage(selenium)
    page.enter_email(x)
    page.enter_pass("Skillfactory1007")
    page.btn_click()
    time.sleep(1)
    assert page.get_error_massage() == "Неверный логин или пароль"

#4Негативная авторизация с неверным паролем
@pytest.mark.parametrize('x', ["9959967398", "regpostt@mail.ru"], ids=["valid_phone", "valid_mail"])
def test_negative_auth_wrong_passw(selenium, x):
    page = AuthPage(selenium)
    page.enter_email(x)
    page.enter_pass("Skillfactory1008")
    page.btn_click()
    time.sleep(1)
    assert page.get_error_massage() == "Неверный логин или пароль"


#5По умолчанию выбрана форма авторизации по телефону
def test_active_elements(selenium):
   page  = AuthPage(selenium)
   assert page.get_phone_element().get_attribute("class") == "rt-tab rt-tab--small rt-tab--active"
   assert page.get_phone_element().text == 'Телефон'
   assert page.get_mail_element().get_attribute("class") != "rt-tab rt-tab--small rt-tab--active"

#6Смена таб выбора при введении данных
@pytest.mark.parametrize('x', ["9959967398", "regpostt@mail.ru", "gfhgfghf2"], ids=["valid_phone", "valid_mail", "login"])
def test_check_change_active_element(selenium, x):
    page = AuthPage(selenium)
    page.enter_email(x)
    page.enter_pass("Skillfactory1007")
    assert page.get_login_element().get_attribute("class") or page.get_phone_element().get_attribute("class") or page.get_mail_element().get_attribute("class") == "rt-tab " \
                                                                                                             "rt-tab--small rt-tab--active"


#7Тестирование формы "Восстановление пароля"
def test_recovery_page_elements(selenium):
    page = RestorePage(selenium)
    assert page.get_phone_element().is_displayed() == True
    assert page.get_mail_element().is_displayed() == True
    assert page.get_login_element().is_displayed() == True
    assert page.get_ls_element().is_displayed() == True
    assert page.get_login_field().is_displayed() == True
    # assert page.get_kapcha_element().get_attribute("alt") == "Captcha"
    assert page.get_kapcha_element().is_displayed() == True
    assert page.get_reset_btn_element().is_displayed() == True
    assert page.reset_back.is_displayed() == True

#8Тестирование формы "Регистрация"
def test_registration_page_elements(selenium):
    page = AuthPage(selenium)
    page.reg_click()
    assert page.get_first_element().is_displayed() == True
    assert page.get_lastname().is_displayed() == True
    assert page.get_address_element().is_displayed() == True
    assert page.get_region().is_displayed() == True
    assert page.get_passw_element().is_displayed() == True
    assert page.get_passw_confirm_element().is_displayed() == True
    assert page.get_link_confidental_element().is_displayed() == True
    assert page.get_reg_logo_element().is_displayed() == True

#9Тестирование позитивной регистрации
def test_positive_registration(selenium):
    page = AuthPage(selenium)
    page.reg_click()
    page.get_first_element().send_keys("Рааа")
    page.get_lastname().send_keys("ааф")
    page.get_address_element().send_keys("example@email.ru")
    page.get_passw_element().send_keys("Superqwerty123")
    page.get_passw_confirm_element().send_keys("Superqwerty123")
    page.get_reg_btn().click()
    time.sleep(5)
    assert page.get_confirm_element().text == "Подтверждение email"

#10Позитивное тестирование поля имя
@pytest.mark.parametrize('x', ["фф", "ааа", "фф-", "ааааааааааааааааааааааааааааа"])
def test_positive_field_name(selenium, x):
    page = AuthPage(selenium)
    page.reg_click()
    page.get_first_element().send_keys(x)
    page.get_lastname().send_keys("ааф")
    page.get_address_element().send_keys("example@email.ru")
    page.get_passw_element().send_keys("Superqwerty123")
    page.get_passw_confirm_element().send_keys("Superqwerty123")
    page.get_reg_btn().click()
    assert page.get_confirm_element().text == "Подтверждение email"


#11Негативное тестирование поля Имя
def test_negative_field_name(selenium):
    page = AuthPage(selenium)
    page.reg_click()
    name = ["--", "1", "", "@@а", "-а", "а", "аааааааааааааааааааааааааааааа", "fffff"]
    for i in name:
        page.get_first_element().send_keys(i)
        page.get_reg_btn().click()
        assert page.get_reg_name_error().text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

#12Позитивное тестирование поля Фамилия
@pytest.mark.parametrize('x', ["фф", "ааа", "фф-", "ааааааааааааааааааааааааааааа"])
def test_positive_field_lastname(selenium, x):
    page = AuthPage(selenium)
    page.reg_click()
    page.get_first_element().send_keys("слава")
    page.get_lastname().send_keys(x)
    page.get_address_element().send_keys("example@email.ru")
    page.get_passw_element().send_keys("Superqwerty123")
    page.get_passw_confirm_element().send_keys("Superqwerty123")
    page.get_reg_btn().click()
    assert page.get_confirm_element().text == "Подтверждение email"

#13Негативное тестирование поля Фамилия
def test_negative_field_lastname(selenium):
    page = AuthPage(selenium)
    page.reg_click()
    name = ["--", "1", "", "@@а", "-а", "а", "аааааааааааааааааааааааааааааа", "fffff"]
    for i in name:
        page.get_lastname().send_keys(i)
        page.get_reg_btn().click()
        assert page.get_reg_lastname_error().text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

#14Негативный тест разных паролей в форме регистрации
def test_diff_passw_registration(selenium):
    page = AuthPage(selenium)
    page.reg_click()
    page.get_first_element().send_keys("Рааа")
    page.get_lastname().send_keys("ааф")
    page.get_address_element().send_keys("example@email.ru")
    page.get_passw_element().send_keys("Superqwerty123")
    page.get_passw_confirm_element().send_keys("Superqwerty124")
    page.get_reg_btn().click()
    assert page.get_diff_passw_error().text == "Пароли не совпадают"

# # #15 Неверный пароль в форме регистрации
def test_wrong_passw_registration(selenium):
    page = AuthPage(selenium)
    page.reg_click()
    page.get_first_element().send_keys("Рааа")
    page.get_lastname().send_keys("ааф")
    page.get_address_element().send_keys("example@email.ru")
    page.get_passw_element().send_keys("Super")
    page.get_passw_confirm_element().send_keys("Super")
    page.get_reg_btn().click()
    assert page.get_wrong_pass_message().text == "Длина пароля должна быть не менее 8 символов"