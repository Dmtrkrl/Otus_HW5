from hw5.pages.catalog_page import *
from hw5.pages.elements.currency import *


def test_catalog_page_title(driver, base_url):
    driver.get(f'{base_url}{CatalogPage.ADD_URL}')
    BasePage(driver).wait_title_contain(CatalogPage.TITLE)


def test_catalog_page_shop_logo(driver, base_url):
    driver.get(f'{base_url}{CatalogPage.ADD_URL}')
    BasePage(driver).wait_element(CatalogPage.LOGO)


def test_catalog_page_goods_groups(driver, base_url):
    driver.get(f'{base_url}{CatalogPage.ADD_URL}')
    BasePage(driver).wait_element(CatalogPage.GOODS_GROUPS)


def test_catalog_page_check_description_field(driver, base_url):
    driver.get(f'{base_url}{CatalogPage.ADD_URL}')
    BasePage(driver).wait_element(CatalogPage.DESCRIPTION_FIELD)


def test_catalog_page_image_field(driver, base_url):
    driver.get(f'{base_url}{CatalogPage.ADD_URL}')
    BasePage(driver).wait_element(CatalogPage.IMAGE_FIELD)


def test_switch_all_currency(driver, base_url):
    driver.get(f'{base_url}{CatalogPage.ADD_URL}')
    for currency in Currency(driver).CURRENCY_DATA:
        initial_price, new_price = Currency(driver).switch_currency(currency)
        assert Currency(driver).wait_element(currency.check)
        assert initial_price != new_price
