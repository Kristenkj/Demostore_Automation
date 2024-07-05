import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFOptions


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
    elif browser_name == ('headlesschrome'):
        chrome_options = ChOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == 'headlessfirefox':
        ff_options = FFOptions()
        ff_options.add_argument("--disable-gpu")
        ff_options.add_argument("--no-sandbox")
        ff_options.add_argument("--headless")
        driver = webdriver.Firefox(options=ff_options)

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
