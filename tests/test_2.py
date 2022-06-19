from Pages.UserPage import UserPage


class Test2:
    def test_deposit_zero(self, efetuar_login):
        home_page = efetuar_login
        user_page = UserPage(home_page.driver)
        assert user_page.is_page(user_page.url_account), "User page not found"
        user_page.select_operation(user_page.btn_deposit_xPath)
        user_page.informar_valor(0)
        assert user_page.confirmar_operacao(0), 'Valor do balanco foi alterado'
