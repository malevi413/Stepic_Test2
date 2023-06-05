from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_MAIL_AUTH = (By.NAME, "login-username")
    LOGIN_PASS_AUTH = (By.NAME, "login-password")
    BTN_FORGET_PASS = (By.LINK_TEXT, "Я забыл пароль")
    LOGIN_ENTER = (By.NAME, "login_submit")

    LOGIN_MAIL_REG = (By.NAME, "registration-email")
    LOGIN_PASS_REG = (By.NAME, "registration-password1")
    LOGIN_PASS_REG_2 = (By.NAME, "registration-password2")
    LOGIN_ENTER_REG = (By.NAME, "registration_submit")


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner > p > strong ")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, "div.alertinner > strong")