from selenium.webdriver.common.by import By
from hw5.pages.base_page import BasePage


class CatalogPage(BasePage):
    ADD_URL = r'/desktops'
    TITLE = 'Desktops'
    LOGO = (By.CSS_SELECTOR, 'img[title="Your Store"]')
    GOODS_GROUPS = (By.CSS_SELECTOR, 'div[class="list-group"]')
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, 'div[class="col-sm-10"]')
    IMAGE_FIELD = (By.CSS_SELECTOR, 'div[class="col-sm-2"]')
