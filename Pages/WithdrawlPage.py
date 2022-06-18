#
from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class WithdrawlPage(PageObject):

    fld_amount = "form-control"
    txt_sucesso = "Transaction successful"
    txt_falha = "Transaction Failed. You can not withdraw amount more than the balance."
    account_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account"

    def __init__(self, driver):
        super(WithdrawlPage, self).__init__(driver=driver)

    def informar_valor_retirada(self, amount):
        txt_field = self.driver.find_element(By.CLASS_NAME, self.fld_amount)
        txt_field.send_keys(amount)

    def confirmar_retirada(self):
        self.driver.find_element(By.CLASS_NAME, self.fld_amount).submit()

    def has_success_message(self):
        txt_sucesso = self.driver.find_element(By.CLASS_NAME, self.txt_sucesso)
        if txt_sucesso == self.txt_sucesso:
            return True
        else:
            return False

    def has_fail_message(self):
        txt_falha = self.driver.find_element(By.CLASS_NAME, self.txt_fail)
        if txt_falha == self.txt_falha:
            return True
        else:
            return False