from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.PageObject import PageObject


class LoginPage(PageObject):
    id_login_btn = "login-button"

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser)
        self.open_page()

    def open_page(self):
        self.driver.get(self.url)

    def click_login_btn(self):
        self.driver.find_element(By.ID, self.id_login_btn).click()

    def is_login_url(self):
        return self.is_page(self.url)

    def has_login_btn(self):
        try:
            self.driver.find_element(By.ID, self.id_login_btn)
            return True
        except NoSuchElementException:
            return False

    def has_login_message_error(self):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(
            (By.CLASS_NAME, self.class_error_login)))
        return element.text == self.txt_login_error_message

    def efetuar_login(self, username="standard_user", password="secret_sauce"):
        self.driver.find_element(By.ID, self.id_username).send_keys(username)
        self.driver.find_element(By.ID, self.id_password).send_keys(password)
        self.driver.find_element(By.ID, self.id_login_btn).click()

    def close(self):
        self.driver.quit()
