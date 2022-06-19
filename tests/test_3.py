from Pages.UserPage import UserPage


class Test3:
    def test_deposit_value(self, efetuar_login):
        home_page = efetuar_login
        user_page = UserPage(home_page.driver)
        assert user_page.is_user_page(), "User page not found"
        user_page.select_dp_operation()
        user_page.informar_valor(100)
        assert user_page.confirmar_operacao(100), 'Valor depositado esta diferente do valor esperado'
