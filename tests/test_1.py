#
#criar as contas x y e z
#

import time

import pytest

from Pages.UserPage import UserPage


class Test1:

    @pytest.mark.parametrize("all_browsers", ["chrome"])
    def test_click_login_btn(self, open_all_browsers):
        home_page = open_all_browsers
        home_page.open_user_login()
        home_page.select_user()
        home_page.login()
        time.sleep(1)
        assert not home_page.is_login_url(), "Página incorreta"
        user_page = UserPage(home_page.driver)
        assert user_page.is_user_page()