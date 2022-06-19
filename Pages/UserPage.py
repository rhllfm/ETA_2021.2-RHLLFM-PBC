# Tela do usuário logado
import time

from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class UserPage(PageObject):
    url_account = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account"
    url_transaction = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx"
    client_title = "fontBig"
    client_name = "Harry Potter"
    btn_transaction_xPath = "/html/body/div/div/div[2]/div/div[3]/button[1]"
    btn_withdrawl_xPath = "/html/body/div/div/div[2]/div/div[3]/button[3]"
    btn_deposit_xPath = "/html/body/div/div/div[2]/div/div[3]/button[2]"
    label_amount_xPath = "/html/body/div/div/div[2]/div/div[4]/div/form/div/label"
    field_amount_xPath = "/html/body/div/div/div[2]/div/div[4]/div/form/div/input"
    field_amount_DP = "Amount to be Deposited :"
    field_amount_WD = "Amount to be Withdrawn :"
    balance_xPath = "/html/body/div/div/div[2]/div/div[2]/strong[2]"
    btn_confirm_deposit_withdrawl = "btn-default"
    id_table_list_transaction = "anchor0"
    btn_reset_xPath = "/html/body/div[1]/div/div[2]/div/div[1]/button[2]"
    valorRetirada = 1
    valorDeposito = 10

    def __init__(self, driver):
        super(UserPage, self).__init__(driver=driver)

    def select_operation(self, operation):
        if operation == self.btn_deposit_xPath:
            self.driver.find_element(By.XPATH, self.btn_deposit_xPath).click()
            time.sleep(2)
        elif operation == self.btn_withdrawl_xPath:
            self.driver.find_element(By.XPATH, self.btn_withdrawl_xPath).click()
            time.sleep(2)
        elif operation == self.btn_transaction_xPath:
            self.driver.find_element(By.XPATH, self.btn_transaction_xPath).click()
            time.sleep(2)

    def check_balance(self):
        balance = self.driver.find_element(By.XPATH, self.balance_xPath).text
        return balance

    def informar_valor(self, amount):
        txt_field = self.driver.find_element(By.XPATH, self.field_amount_xPath)
        txt_field.send_keys(amount)

    def confirmar_operacao(self, valor):
        valor_anterior = int(self.check_balance())
        self.driver.find_element(By.CLASS_NAME, self.btn_confirm_deposit_withdrawl).submit()
        valor_atual = int(self.check_balance())
        if valor_anterior > valor_atual:
            print("A retirada foi realizada com sucesso")
            return valor_anterior - valor_atual == valor
        elif valor_anterior < valor_atual:
            print("O depósito foi realizado com sucesso")
            return valor_atual - valor_anterior == valor
        elif valor_anterior == valor_atual:
            print("Valor depositado/retirado é igual a zero")
            return valor_atual - valor_anterior == valor
        else:
            print("Valor informado para retirada é maior que valor do balanço")
            return False

    def reset_transactions(self):
        self.driver.find_element(By.XPATH, self.btn_reset_xPath).click()
        time.sleep(1)

    def get_qtd_transactions(self):
        return len(self.driver.find_elements(By.XPATH, self.id_table_list_transaction))