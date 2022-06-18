# Tela do usuário logado
from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class UserPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    client_title = "fontBig"
    client_name = "Harry Potter"
    deposit_option = "//button[@ng-class='btnClass2']"

    btn_withdrawl_xPath = "/html/body/div/div/div[2]/div/div[3]/button[3]"
    btn_deposit_xPath = "/html/body/div/div/div[2]/div/div[3]/button[2]"
    label_amount_xPath = "/html/body/div/div/div[2]/div/div[4]/div/form/div/label"
    field_amount_xPath = "/html/body/div/div/div[2]/div/div[4]/div/form/div/input"
    field_amount_DP = "Amount to be Deposited :"
    field_amount_WD = "Amount to be Withdrawn :"
    balance_xPath = "/html/body/div/div/div[2]/div/div[2]/strong[2]"
    btn_confirm_deposit_withdrawl = "btn-default"
    url_account = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account"


    def __init__(self, driver):
        super(UserPage, self).__init__(driver=driver)

    def is_user_page(self):
        user_name = self.driver.find_element(By.CLASS_NAME, self.client_title).text
        print(user_name)
        if user_name == self.client_name:
            return self.is_page(self.url)

    def click_deposit_option(self):
        self.driver.find_element(By.XPATH, self.deposit_option).click()

    def select_dp_operation(self):
        self.driver.find_element(By.XPATH, self.btn_deposit_xPath).click()

    def select_wd_operation(self):
        self.driver.find_element(By.XPATH, self.btn_withdrawl_xPath).click()

    # def check_operacao(self):
    #     label_operacao = self.driver.find_element(By.XPATH, self.label_amount_xPath).text
    #     return label_operacao

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
            return valor_anterior-valor_atual == valor
        elif valor_anterior < valor_atual:
            print("O depósito foi realizado com sucesso")
            return valor_atual-valor_anterior == valor
        elif valor_anterior == valor_atual:
            print("Valor depositado/retirado é igual a zero")
            return valor_atual-valor_anterior == valor
        else:
            print("Valor informado para retirada é maior que valor do balanço")
            return False

    def has_success_message(self):
        txt_sucesso = self.driver.find_element(By.CLASS_NAME, self.txt_sucesso)
        if txt_sucesso == self.txt_sucesso:
            return True
        else:
            return False

    def has_fail_message(self):
        txt_falha = self.driver.find_element(By.CLASS_NAME, self.txt_falha)
        if txt_falha == self.txt_falha:
            return True
        else:
            return False