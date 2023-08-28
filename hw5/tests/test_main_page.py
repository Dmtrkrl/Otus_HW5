from hw5.pages.main_page import *
from hw5.pages.elements.currency import *
from hw5.pages.elements.product import *


def test_main_page_title(driver, base_url):
    driver.get(base_url)
    MainPage(driver).wait_title_contain(MainPage.TITLE)


def test_main_page_logo(driver, base_url):
    driver.get(base_url)
    MainPage(driver).wait_element(MainPage.LOGO)


def test_main_page_cart(driver, base_url):
    driver.get(base_url)
    MainPage(driver).wait_element(MainPage.CART)


def test_main_page_search(driver, base_url):
    driver.get(base_url)
    MainPage(driver).wait_element(MainPage.SEARCH)


def test_main_page_goods(driver, base_url):
    driver.get(base_url)
    MainPage(driver).wait_element(MainPage.SLIDE_SHOW)


def test_switch_all_currency(driver, base_url):
    driver.get(base_url)
    for currency in Currency(driver).CURRENCY_DATA:
        initial_price, new_price = Currency(driver).switch_currency(currency)
        assert Currency(driver).wait_element(currency.check)
        assert initial_price != new_price


def test_add_product_to_cat(driver, base_url):
    driver.get(base_url)
    selected_product = ProductPage(driver).add_to_cart()
    item_product = ProductPage(driver).check_item_name()
    assert selected_product == item_product
