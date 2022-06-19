import time

import pytest
from pip._internal.utils import datetime

from Pages.UserPage import UserPage

class Test4:

    @pytest.mark.parametrize("browser", ["chrome"])
    def test_verificar_transacao(self, efetuar_login):
        home_page = efetuar_login
        user_page = UserPage(home_page.driver)
        user_page.select_operation(user_page.btn_deposit_xPath)
        user_page.informar_valor(user_page.valorDeposito)
        assert user_page.confirmar_operacao(user_page.valorDeposito), "Deposited value is different from the expected."
        user_page.select_operation(user_page.btn_transaction_xPath)
        assert user_page.is_page(user_page.url_transaction), "Transaction page not found"
        user_page.set_search_interval("2022-06-10T00:00:00", "2022-06-19T01:05:59")
        assert user_page.check_transations_table(), "Transactions should be listed"
        user_page.reset_transactions()
        assert not user_page.check_transations_table(), "Transactions should NOT be listed"
