from selenium.webdriver.common.by import By
from hw5.pages.base_page import BasePage
from hw5.pages.elements.user_data import NewUser


class RegisterPage(BasePage):
    ADD_URL = 'index.php?route=account/register'
    TITLE = 'Register Account'

    FIRST_NAME_FIELD = (By.CSS_SELECTOR, 'input[type="text"][name="firstname"]')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, 'input[type="text"][name="lastname"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[type="email"][name="email"]')
    PHONE_FIELD = (By.CSS_SELECTOR, 'input[type="tel"][name="telephone"]')

    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[type="password"][name="password"]')
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[type="password"][name="confirm"]')

    SUBSCRIBE_BTN = (By.CSS_SELECTOR, 'input[type="radio"][name="newsletter"]')
    PRIVACY_CHECKBOX_BTN = (By.CSS_SELECTOR, 'input[type="checkbox"][name="agree"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"][value="Continue"]')

    ACCEPT_REGISTRATION = (By.XPATH, '//h1[contains(text(),"Your Account Has Been Created!")]')

    def input_first_name(self):
        self.wait_element(self.FIRST_NAME_FIELD).send_keys(NewUser.FIRST_NAME)

    def input_last_name(self):
        self.wait_element(self.LAST_NAME_FIELD).send_keys(NewUser.LAST_NAME)

    def input_email(self):
        self.wait_element(self.EMAIL_FIELD).send_keys(NewUser.EMAIL)

    def input_phone(self):
        self.wait_element(self.PHONE_FIELD).send_keys(NewUser.PHONE)

    def input_password(self):
        self.wait_element(self.PASSWORD_FIELD).send_keys(NewUser.PASSWORD)
        self.wait_element(self.CONFIRM_PASSWORD_FIELD).send_keys(NewUser.PASSWORD)

    def click_privacy(self):
        self.click(self.PRIVACY_CHECKBOX_BTN)

    def click_continue_for_registration(self):
        self.click(self.CONTINUE_BUTTON)

    def checking_registration(self):
        self.wait_element(self.ACCEPT_REGISTRATION)
