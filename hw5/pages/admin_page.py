from selenium.webdriver.common.by import By
from hw5.pages.base_page import BasePage
from hw5.pages.elements.admin_login import *
from hw5.helpers import random_string, random_price


class AdminPage(BasePage):
    ADD_URL = 'admin/'
    TITLE = 'Administration'

    USERNAME_FIELD = (By.CSS_SELECTOR, 'input[name="username"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="password"]')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')
    FORGOTTEN_BTN = (By.CSS_SELECTOR, 'span[class="help-block"]')

    CATALOG_BTN = (By.LINK_TEXT, 'Catalog')
    PRODUCT_BTN = (By.LINK_TEXT, 'Products')
    ADD_NEW_PRODUCT_BTN = (By.CSS_SELECTOR, '[data-original-title="Add New"]')

    PRODUCT_NAME = (By.CSS_SELECTOR, 'input[name="product_description[1][name]"]')
    PRODUCT_METE_TAG_TITLE = (By.CSS_SELECTOR, 'input[name="product_description[1][meta_title]"]')
    DATA_TAB = (By.LINK_TEXT, 'Data')
    MODEL = (By.CSS_SELECTOR, 'input[name="model"]')
    PRICE = (By.CSS_SELECTOR, 'input[name="price"]')
    SAVE_BTN = (By.CSS_SELECTOR, '[data-original-title="Save"]')

    FILTER_BY_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="filter_name"]')
    FILTER_BTN = (By.CSS_SELECTOR, 'button[id="button-filter"]')
    PRODUCT_FIND = (By.CSS_SELECTOR, 'td[class="text-center"]')
    NO_RESULT = (By.XPATH, '//td[contains(text(),"No results!")]')

    SELECT_PRODUCT = (By.CSS_SELECTOR, 'input[name="selected[]"]')
    PRODUCT_DELETE_BTN = (By.CSS_SELECTOR, '.btn-danger')

    def admin_login(self):
        self.wait_element(self.USERNAME_FIELD).send_keys(Admin.LOGIN)
        self.wait_element(self.PASSWORD_FIELD).send_keys(Admin.PASSWORD)
        self.click(self.LOGIN_BTN)

    def open_catalog(self):
        [self.click(btn) for btn in (self.CATALOG_BTN, self.PRODUCT_BTN)]

    def create_product(self):
        self.click(self.ADD_NEW_PRODUCT_BTN)

    def add_new_product_info(self):
        self.wait_element(self.PRODUCT_NAME).send_keys(Product.NAME)
        self.wait_element(self.PRODUCT_METE_TAG_TITLE).send_keys(Product.METE_TAG_TITLE)
        self.click(self.DATA_TAB)
        self.wait_element(self.MODEL).send_keys(Product.MODEL)
        self.wait_element(self.PRICE).send_keys(Product.PRICE)
        self.click(self.SAVE_BTN)

    def find_product(self):
        self.wait_element(self.FILTER_BY_NAME_FIELD).send_keys(Product.NAME)
        self.click(self.FILTER_BTN)

    def delete_product(self):
        self.click(self.SELECT_PRODUCT)
        self.click(self.PRODUCT_DELETE_BTN)
        self.accept_allert()

    def check_add_product(self):
        assert len(self.wait_elements(self.PRODUCT_FIND)) > 3, 'Product not added!'

    def check_del_product(self):
        assert self.wait_element(self.NO_RESULT).text == 'No results!', 'Product not deleted!'


class DashboardPage(BasePage):
    LOGOUT_BTN = (By.CSS_SELECTOR, 'i[class="fa fa-sign-out"]')


class Product:
    NAME = random_string()
    METE_TAG_TITLE = random_string()
    MODEL = random_string()
    PRICE = random_price()
