from Pages.UserPage import UserPage
import pytest

class Test3:

    @pytest.mark.parametrize("browser", ["chrome"])
    def test_deposit_value(self, efetuar_login):
        home_page = efetuar_login
        user_page = UserPage(home_page.driver)
        user_page.select_operation(user_page.btn_deposit_xPath)
        user_page.informar_valor(100)
        assert user_page.confirmar_operacao(100), "Deposited value is different from the expected."