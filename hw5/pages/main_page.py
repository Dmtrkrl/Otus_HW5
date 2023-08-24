from selenium.webdriver.common.by import By
from hw5.pages.base_page import BasePage


class MainPage(BasePage):
    TITLE = 'Your Store'
    LOGO = (By.CSS_SELECTOR, 'img[title="Your Store"]')
    CART = (By.CSS_SELECTOR, 'div[class="btn-group btn-block"]')
    SEARCH = (By.CSS_SELECTOR, 'input[name="search"]')
    SLIDE_SHOW = (By.CSS_SELECTOR, 'div[class="swiper-wrapper"]')
    ADD_PRODUCT_BTN = (By.CSS_SELECTOR, 'i[class="fa fa-shopping-cart"]')
