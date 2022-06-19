import time
import pytest

from Pages.UserPage import UserPage

class Test6:

    @pytest.mark.parametrize("browser", UserPage.browsers_list)
    def test_withdrawl_success(self, efetuar_login):
        home_page = efetuar_login
        user_page = UserPage(home_page.driver)
        user_page.select_operation(user_page.btn_withdrawl_xPath)
        time.sleep(1)
        user_page.informar_valor(user_page.valorRetirada)
        time.sleep(1)
        assert not user_page.confirmar_operacao(user_page.valorRetirada), "Operação falhou"
        time.sleep(1)
