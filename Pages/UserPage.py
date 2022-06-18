# Tela do usuário logado

from Pages.PageObject import PageObject


class UserPage(PageObject):

    def __init__(self, driver):
        super(UserPage, self).__init__(driver=driver)
