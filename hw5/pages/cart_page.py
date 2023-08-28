from selenium.webdriver.common.by import By
from hw5.pages.base_page import BasePage


class CartPage(BasePage):
    ADD_URL = r'index.php?route=checkout/cart'
    TITLE = 'Shopping Cart'
    LOGO = (By.CSS_SELECTOR, 'img[title="Your Store"]')
    SEARCH = (By.CSS_SELECTOR, 'input[name="search"]')
    CONTENT_FIELD = (By.CSS_SELECTOR, 'div[id="content"]')
    CONTINUE_BTN = (By.CSS_SELECTOR, 'div[class="pull-right"]')
