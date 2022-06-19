from Pages.UserPage import UserPage


class Test4:
    def test_verificar_transacao(self, efetuar_login):
        home_page = efetuar_login
        user_page = UserPage(home_page.driver)
        assert user_page.is_user_page(), "User page not found"
        user_page.select_dp_operation()
        user_page.informar_valor(50)
        user_page.confirmar_operacao(50)
        time.sleep(2)
        user_page.select_ts_operation()
        time.sleep(2)
        assert user_page.get_qtd_transactions() == 1, 'Quantidade de transacões incorreta'
        user_page.click_reset_button()
        assert user_page.get_qtd_transactions() == 0, 'Transações nao foram resetadas'


