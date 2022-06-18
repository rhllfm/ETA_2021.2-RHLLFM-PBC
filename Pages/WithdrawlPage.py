#
from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class WithdrawlPage(PageObject):

    def __init__(self, driver):
        super(WithdrawlPage, self).__init__(driver=driver)

