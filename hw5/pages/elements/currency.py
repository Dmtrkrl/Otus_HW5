from selenium.webdriver.common.by import By
from hw5.pages.base_page import BasePage
from collections import namedtuple
import re


class Currency(BasePage):
    CURRENCY_BTN = (By.CSS_SELECTOR, '[class="fa fa-caret-down"]')
    EUR = (By.NAME, 'EUR')
    IS_EUR_CURRENCY = (By.XPATH, '//strong[text()="€"]')
    GBP = (By.NAME, 'GBP')
    IS_GBP_CURRENCY = (By.XPATH, '//strong[text()="£"]')
    USD = (By.NAME, 'USD')
    IS_USD_CURRENCY = (By.XPATH, '//strong[text()="$"]')

    CURRENCY = namedtuple('Currency', 'name, check')
    CURRENCY_DATA = (
        CURRENCY(name=EUR, check=IS_EUR_CURRENCY),
        CURRENCY(name=GBP, check=IS_GBP_CURRENCY),
        CURRENCY(name=USD, check=IS_USD_CURRENCY)
    )

    @property
    def get_product_price(self):
        price_element = self.driver.find_element(By.CSS_SELECTOR, 'p.price')
        price_text = price_element.text.strip()
        currency_patterns = {
            '$': r'\$([\d,.]+)',
            '€': r'([\d,.]+)\s?€',
            '£': r'([\d,.]+)\s?£'
        }
        for money_symbol, pattern in currency_patterns.items():
            match = re.search(pattern, price_text)
            if match:
                value = float(match.group(1).replace(',', ''))
                return value
        return None

    def switch_currency(self, currency):
        initial_price = self.get_product_price
        self.click(self.CURRENCY_BTN)
        self.click(currency.name)
        new_price = self.get_product_price
        return initial_price, new_price
