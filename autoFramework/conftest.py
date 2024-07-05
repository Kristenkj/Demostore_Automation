import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def setup(request, browser_name, url):
    if browser_name == 'chrome':
        driver = webdriver.Chrome()
    elif browser_name == ('firefox', 'ff'):
        driver = webdriver.Firefox()
    elif browser_name == 'edge':
        driver = webdriver.Edge()
    elif browser_name == 'IE':
        driver = webdriver.Ie()

    driver.get(url)
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption("--url", default="http://demostore.supersqa.com")


@pytest.fixture(scope="class", autouse=True)
def browser_name(request):
    return request.config.getoption("--browser_name")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")
