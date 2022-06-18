#tela inicial
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.PageObject import PageObject


class HomePage(PageObject):

    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    ng_login_user = "customer"
    ng_customer_login_txt = "Customer Login"
    ng_manager_login_txt = "Bank Manager Login"
    button_class_name = "btn-lg"
    button_customer_css = "div > button[name='Customer Login']"
    user_class_name = "ng-binding"
    default_user = "Harry Potter"
    user_select_form = "userSelect"
    btn_login = "btn-default"

    def __init__(self, browser):
        super(HomePage, self).__init__(browser)
        self.open_page()

    def open_page(self):
        self.driver.get(self.url)

    def is_login_url(self):
        return self.is_page(self.url)

    def open_user_login(self):
        btn_list = self.driver.find_elements(By.CLASS_NAME, self.button_class_name)
        for btn in btn_list:
            if btn.text==self.ng_customer_login_txt:
                print(btn)
                btn.click()

    def select_user(self):
        locator_select_customer = (By.NAME, self.user_select_form)
        time.sleep(1)
        select_elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator_select_customer))
        time.sleep(1)
        Select(select_elem).select_by_visible_text(self.default_user)

    def login(self):
        self.driver.find_element(By.CLASS_NAME, self.btn_login).submit()

    def close(self):
        self.driver.quit()