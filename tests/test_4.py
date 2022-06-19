from Pages.UserPage import UserPage


class Test4:
    def test_verificar_transacao(self, efetuar_login):
        home_page = efetuar_login
        user_page = UserPage(home_page.driver)
        assert user_page.is_user_page(), "User page not found"
        user_page.select_dp_operation()
        user_page.informar_valor(50)
        assert user_page.confirmar_operacao(50), 'Valor do balanco foi alterado'
        user_page.select_ts_operation()
        assert user_page.is_user_page(), "Transaction page not found"

