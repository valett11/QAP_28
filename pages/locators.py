from selenium.webdriver.common.by import By

class AuthLocators:
    AUTH_PHONE = (By.ID, "username")
    AUTH_EMAIL = (By.ID, "username")
    AUTH_PASS = (By.ID, "password")
    AUTH_BTN = (By.ID, "kc-login")
    REG_LINK = (By.ID, "kc-register")
    PHONE_TAB_ELEMENT = (By.ID, "t-btn-tab-phone")
    MAIL_TAB_ELEMENT = (By.ID, "t-btn-tab-mail")
    LOGIN_TAB_ELEMENT = (By.ID, "t-btn-tab-login")
    LS_TAB_ELEMENT = (By.ID, "t-btn-tab-ls")
    LOGO_ELEMENT = (By.CSS_SELECTOR, "#page-left > div > div.what-is-container__logo-container > svg")
    INFO_ELEMENT = (By.CSS_SELECTOR, "#page-left > div > div.what-is")
    FOGOT_PASSW = (By.ID, "forgot_password")
    ERROR_AUTH = (By.ID, "form-error-message")