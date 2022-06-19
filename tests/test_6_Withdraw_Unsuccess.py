#
#Fazer retirada
#
import time
import pytest
from Pages.UserPage import UserPage

class Test1:

    @pytest.mark.parametrize("browser", ["chrome"])
    def test_withdrawl_success(self, efetuar_login):
        home_page = efetuar_login
        user_page = UserPage(home_page.driver)
        user_page.select_operation(user_page.btn_withdrawl_xPath)
        time.sleep(1)
        user_page.informar_valor(user_page.valorRetirada)
        time.sleep(1)
        assert not user_page.confirmar_operacao(user_page.valorRetirada), "Operação falhou"
        time.sleep(1)
