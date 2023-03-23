from selenium.webdriver.common.by import By

class AuthLocators:
    AUTH_PHONE = (By.ID, "username")
    AUTH_EMAIL = (By.ID, "username")
    AUTH_PASS = (By.ID, "password")
    AUTH_BTN = (By.ID, "kc-login")

