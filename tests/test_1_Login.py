import time
import pytest

from Pages.UserPage import UserPage


class Test1:

    @pytest.mark.parametrize("browser", UserPage.browsers_list)
    def test_click_login_btn(self, open_browser):
        home_page = open_browser
        assert home_page.is_page(home_page.url_login)
        time.sleep(1)
        home_page.open_user_login()
        home_page.select_user()
        home_page.login()
        user_page = UserPage(home_page.driver)
        assert user_page.is_page(user_page.url_account)
        time.sleep(1)