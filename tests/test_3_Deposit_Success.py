import pytest
from Pages.UserPage import UserPage

class Test3:

    @pytest.mark.parametrize("browser", UserPage.browsers_list)
    def test_deposit_value(self, efetuar_login):
        home_page = efetuar_login
        user_page = UserPage(home_page.driver)
        assert user_page.is_page(user_page.url_account), "User page not found"
        user_page.select_operation(user_page.btn_deposit_xPath)
        user_page.informar_valor(100)
        assert user_page.confirmar_operacao(100), 'Valor depositado esta diferente do valor esperado'
