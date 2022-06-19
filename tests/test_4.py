import time

import pytest

from Pages.UserPage import UserPage

class Test4:

    @pytest.mark.parametrize("browser", ["chrome"])
    def test_verificar_transacao(self, efetuar_login):
        home_page = efetuar_login
        user_page = UserPage(home_page.driver)
        user_page.select_operation(user_page.btn_deposit_xPath)
        user_page.informar_valor(user_page.valorDeposito)
        assert user_page.confirmar_operacao(user_page.valorDeposito), "Deposited value is different from the expected."
        user_page.informar_valor(user_page.valorDeposito)
        assert user_page.is_page(user_page.url_transaction), "Transaction page not found"
        assert user_page.get_qtd_transactions() == 1, 'Quantidade de transacões incorreta'
        user_page.reset_transactions()
        assert user_page.get_qtd_transactions() == 0, 'Transações nao foram resetadas'