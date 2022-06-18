#
#criar as contas x y e z
#

import time

import pytest


class Test1:

    @pytest.mark.parametrize("all_browsers", ["chrome"])
    def test_click_login_btn(self, open_all_browsers):
        home_page = open_all_browsers
        home_page.open_user_login()
        home_page.select_user()
        time.sleep(1)
        home_page.login()
        time.sleep(2)
        assert home_page.is_login_url(), "Página incorreta"
        assert home_page.has_login_message_error(), "Mensagem de erro não encontrada!"