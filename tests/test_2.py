from Pages.UserPage import UserPage


class Test2:
    def test_deposit_zero(self, efetuar_login):
        home_page = efetuar_login
        user_page = UserPage(home_page.driver)
        assert user_page.is_user_page(), "User page not found"
        user_page.select_dp_operation()
        user_page.informar_valor(0)
        assert user_page.confirmar_operacao(0), 'Valor do balanco foi alterado'
