# Tela de login para selecionar o usuário
from Pages.PageObject import PageObject


class CustomerLoginPage(PageObject):

    def __init__(self, driver):
        super(CustomerLoginPage, self).__init__(driver=driver)
