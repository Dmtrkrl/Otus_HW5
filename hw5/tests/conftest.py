import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.31.210:8081/")


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        service = ChromiumService()
        browser = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = FFService()
        browser = webdriver.Firefox(service=service)
    else:
        raise ValueError(f'Browser {browser_name} not supported!')

    browser.maximize_window()

    request.addfinalizer(browser.close)

    return browser
