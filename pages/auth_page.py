from .base_page import BasePage
from .locators import AuthLocators

import time

class AuthPage(BasePage):

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        url = "https://b2c.passport.rt.ru/"
        driver.get(url)
        self.phone = driver.find_element(*AuthLocators.AUTH_PHONE)
        self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
        self.passw = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.reg = driver.find_element(*AuthLocators.REG_LINK)
        self.phone_element = driver.find_element(*AuthLocators.PHONE_ELEMENT)
        # time.sleep(1)

    def get_phone_element(self):
        return self.phone_element

    def enter_phone(self, value):
        self.email.send_keys(value)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_pass(self, value):
        self.passw.send_keys(value)

    def btn_click(self):
        self.btn.click()

    def reg_click(self):
        self.reg.click()

    def phone_element_click(self):
        self.phone_element.click()