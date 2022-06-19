#
#Fazer retirada
#
import time
import pytest
from Pages.UserPage import UserPage

class Test5:

    @pytest.mark.parametrize("browser", ["chrome"])
    def test_withdrawl_success(self, efetuar_login):
        home_page = efetuar_login
        user_page = UserPage(home_page.driver)
        user_page.select_operation(user_page.btn_deposit_xPath)
        user_page.informar_valor(user_page.valorDeposito)
        assert user_page.confirmar_operacao(user_page.valorDeposito), "Deposited value is different from the expected."
        time.sleep(1)
        user_page.select_operation(user_page.btn_withdrawl_xPath)
        time.sleep(1)
        user_page.informar_valor(user_page.valorRetirada)
        time.sleep(1)

        assert user_page.confirmar_operacao(user_page.valorRetirada), "Operação falhou"
        time.sleep(1)