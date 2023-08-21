from selenium.webdriver.common.by import By
from hw5.pages.framework import PseudoFramework


class RegisterPage(PseudoFramework):
    ADD_URL = 'index.php?route=account/register'
    TITLE = 'Register Account'
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, 'input[type="text"][name="firstname"]')
    SUBSCRIBE_BTN = (By.CSS_SELECTOR, 'input[type="radio"][name="newsletter"]')
    PRIVACY_CHECKBOX_BTN = (By.CSS_SELECTOR, 'input[type="checkbox"][name="agree"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"][value="Continue"]')
