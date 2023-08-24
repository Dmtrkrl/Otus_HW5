from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def wait_title_contain(self, text, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(ec.title_contains(text))
        except TimeoutException:
            raise AssertionError(f'Not wait {text} in page title')

    def wait_elements(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f'Not wait {locator} in page')

    def wait_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f'Not wait {locator} in page')

    def element(self, locator):
        return self.wait_element(locator=locator)

    def click(self, locator):
        element = self.element(locator)
        ActionChains(self.driver).pause(0.3).move_to_element(element).click().perform()

    def accept_allert(self):
        self.driver.switch_to.alert.accept()
