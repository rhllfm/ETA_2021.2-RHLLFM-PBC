#
#criar as contas x y e z
#

import time

import pytest


class Test1:
    customer_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account"

    @pytest.mark.parametrize("all_browsers", ["chrome"])
    def test_click_login_btn(self, open_all_browsers):
        home_page = open_all_browsers
        home_page.open_user_login()
        home_page.select_user()
        home_page.login()
        time.sleep(1)
        assert home_page.is_page(self.customer_url), "Página incorreta"