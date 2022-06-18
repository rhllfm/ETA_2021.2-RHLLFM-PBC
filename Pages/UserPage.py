# Tela do usuário logado
from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class UserPage(PageObject):

    btn_withdrawl_xPath = "/html/body/div/div/div[2]/div/div[3]/button[3]"

    def __init__(self, driver):
        super(UserPage, self).__init__(driver=driver)

    def select_wd_operation(self):
        self.driver.find_element(By.XPATH, self.btn_withdrawl_xPath).click()