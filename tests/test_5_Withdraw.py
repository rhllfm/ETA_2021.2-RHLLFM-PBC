#
#Fazer retirada
#

import time

import pytest

from Pages.UserPage import UserPage
from Pages.WithdrawlPage import WithdrawlPage


class Test1:

    valor = 1

    account_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account"
    @pytest.mark.parametrize("all_browsers", ["chrome"])
    def test_withdrawl_success(self, open_all_browsers):
        home_page = open_all_browsers
        home_page.open_user_login()
        home_page.select_user()
        home_page.login()
        time.sleep(1)
        assert home_page.is_page(self.account_url), "Página incorreta"
        user_page = UserPage(home_page.driver)
        user_page.select_wd_operation()
        withdrawl_page = WithdrawlPage(user_page.driver)
        withdrawl_page.informar_valor_retirada(self.valor)
        withdrawl_page.confirmar_retirada()
        assert withdrawl_page.has_success_message(), "Depósito não foi concluído com sucesso"
        assert not withdrawl_page.has_fail_message(), "Depósito foi aprovado indevidamente"