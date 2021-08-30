import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="what browser to use")

@pytest.fixture(scope='session')
def driver(request):
    browser_type = request.config.getoption('--browser')
    if browser_type == "Firefox" or browser_type == "firefox":
        driver = webdriver.Firefox()
    elif browser_type == "Chrome" or browser_type == "chrome":
        driver =  webdriver.Chrome()
    else:
        raise ValueError(f"Browser type {browser_type} not supported, choose Firefox or Chrome.")
    
    yield driver

    driver.close()
    