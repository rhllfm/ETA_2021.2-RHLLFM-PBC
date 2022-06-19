#
#Fazer retirada
#

import time

import pytest

from Pages.DepositPage import DepositPage
from Pages.UserPage import UserPage
from Pages.WithdrawlPage import WithdrawlPage


class Test1:

    valorRetirada = 1
    valorDeposito = 10
    account_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account"
    operacao_true = "Operação não foi concluída com sucesso."
    operacao_false = "Oparação foi concluída indevidamente."


    @pytest.mark.parametrize("all_browsers", ["chrome"])
    def test_withdrawl_success(self, open_all_browsers):
        home_page = open_all_browsers
        home_page.open_user_login()
        home_page.select_user()
        home_page.login()
        time.sleep(1)
        assert home_page.is_login_url(), "Página incorreta"
        user_page = UserPage(home_page.driver)

        user_page.select_dp_operation(), "Operação de depósito indisponível"
        user_page.informar_valor(self.valorDeposito)
        time.sleep(1)
        assert user_page.confirmar_operacao(self.valorDeposito), "Operação falhou"
        time.sleep(1)
        user_page.select_wd_operation(), "Operação de retirada indisponível!"
        time.sleep(1)
        user_page.informar_valor(self.valorRetirada)
        time.sleep(1)

        assert user_page.confirmar_operacao(self.valorRetirada), "Operação falhou"
        time.sleep(1)