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
def efetuar_login(open_browser):
    home_page = open_browser
    home_page.open_user_login()
    home_page.select_user()
    home_page.login()
    yield home_page
