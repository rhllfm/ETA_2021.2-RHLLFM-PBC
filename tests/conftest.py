import pytest

from Pages.HomePage import HomePage


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser to run the tests")

@pytest.fixture
def browser(request):
    select_browser = request.config.getoption("browser").lower()
    yield select_browser

@pytest.fixture()
def open_browser(browser):
    home_page = HomePage(browser=browser)
    yield home_page
    home_page.close()

@pytest.fixture()
def open_all_browsers(all_browsers):
    home_page = HomePage(browser=all_browsers)
    yield home_page
    home_page.close()