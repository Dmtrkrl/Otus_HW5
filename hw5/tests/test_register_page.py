from hw5.pages.base_page import BasePage
from hw5.pages.register_page import RegisterPage


def test_register_page_title(driver, base_url):
    driver.get(f'{base_url}{RegisterPage.ADD_URL}')
    BasePage(driver).wait_title_contain(RegisterPage.TITLE)


def test_register_page_name_field(driver, base_url):
    driver.get(f'{base_url}{RegisterPage.ADD_URL}')
    BasePage(driver).wait_element(RegisterPage.FIRST_NAME_FIELD)


def test_register_page_subscribe_btn(driver, base_url):
    driver.get(f'{base_url}{RegisterPage.ADD_URL}')
    BasePage(driver).wait_element(RegisterPage.SUBSCRIBE_BTN)


def test_register_page_privacy_checkbox_btn(driver, base_url):
    driver.get(f'{base_url}{RegisterPage.ADD_URL}')
    BasePage(driver).wait_element(RegisterPage.PRIVACY_CHECKBOX_BTN)


def test_register_page_continue_btn(driver, base_url):
    driver.get(f'{base_url}{RegisterPage.ADD_URL}')
    BasePage(driver).wait_element(RegisterPage.CONTINUE_BUTTON)


def test_registration_new_user(driver, base_url):
    driver.get(f'{base_url}{RegisterPage.ADD_URL}')
    RegisterPage(driver).input_first_name()
    RegisterPage(driver).input_last_name()
    RegisterPage(driver).input_email()
    RegisterPage(driver).input_phone()
    RegisterPage(driver).input_password()
    RegisterPage(driver).click_privacy()
    RegisterPage(driver).click_continue_for_registration()
    RegisterPage(driver).checking_registration()
