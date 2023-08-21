from hw5.pages.admin_page import *
from hw5.pages.elements.admin_login import *


def test_admin_page_title(driver, base_url):
    driver.get(f'{base_url}{AdminPage.ADD_URL}')
    PseudoFramework(driver).wait_title_contain(AdminPage.TITLE)


def test_admin_page_username_field(driver, base_url):
    driver.get(f'{base_url}{AdminPage.ADD_URL}')
    PseudoFramework(driver).wait_element(AdminPage.USERNAME_FIELD)


def test_admin_page_password_field(driver, base_url):
    driver.get(f'{base_url}{AdminPage.ADD_URL}')
    PseudoFramework(driver).wait_element(AdminPage.PASSWORD_FIELD)


def test_admin_page_login_btn(driver, base_url):
    driver.get(f'{base_url}{AdminPage.ADD_URL}')
    PseudoFramework(driver).wait_element(AdminPage.LOGIN_BTN)


def test_admin_page_forgotten_btn(driver, base_url):
    driver.get(f'{base_url}{AdminPage.ADD_URL}')
    PseudoFramework(driver).wait_element(AdminPage.LOGIN_BTN)


def test_admin_login(driver, base_url):
    driver.get(f'{base_url}{AdminPage.ADD_URL}')
    PseudoFramework(driver).wait_element(AdminPage.USERNAME_FIELD).send_keys(Admin.LOGIN)
    PseudoFramework(driver).wait_element(AdminPage.PASSWORD_FIELD).send_keys(Admin.PASSWORD)
    PseudoFramework(driver).click(AdminPage.LOGIN_BTN)
    PseudoFramework(driver).wait_element(DashboardPage.LOGOUT_BTN)
