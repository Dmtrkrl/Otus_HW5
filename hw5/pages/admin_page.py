from selenium.webdriver.common.by import By
from hw5.pages.framework import PseudoFramework


class AdminPage(PseudoFramework):
    ADD_URL = 'admin/'
    TITLE = 'Administration'
    USERNAME_FIELD = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_BTN = (By.CSS_SELECTOR, "span[class='help-block']")


class DashboardPage(PseudoFramework):
    LOGOUT_BTN = (By.CSS_SELECTOR, 'i[class="fa fa-sign-out"]')
