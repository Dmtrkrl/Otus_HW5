from selenium.webdriver.common.by import By
from hw5.pages.base_page import BasePage


class ProductPage(BasePage):
    CART_BTN = (By.CSS_SELECTOR, 'button[type="button"][class="btn btn-inverse btn-block btn-lg dropdown-toggle"]')
    ADD_BTN = (By.CSS_SELECTOR, 'button[onclick="cart.add(\'43\');"]')
    ITEM_DROPDOWN_MENU = (By.CSS_SELECTOR, 'ul[class="dropdown-menu pull-right"]')

    def get_product_name(self):
        name_product = self.driver.find_element(By.CSS_SELECTOR, 'div.caption h4 a')
        name_product_text = name_product.text.strip()
        return name_product_text

    def add_to_cart(self):
        self.click(self.ADD_BTN)
        received_name = self.get_product_name()
        return received_name

    def check_item_name(self):
        self.click(self.CART_BTN)
        self.wait_element(self.ITEM_DROPDOWN_MENU)
        item_name = self.driver.find_element(By.CSS_SELECTOR, 'td.text-left a')
        item_on_cart = item_name.text.strip()
        return item_on_cart
