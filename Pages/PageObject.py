from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class PageObject:
    class_name_title = "title"
    balance_value = "//div[@ng-hide='noAccount'][1]/strong[2]"

    def __init__(self, browser=None, driver=None):
        if driver:
            self.driver = driver
        else:
            if browser == "chrome":
                chrome_driver = ChromeService(executable_path=ChromeDriverManager().install())
                self.driver = webdriver.Chrome(service=chrome_driver)
            elif browser == "firefox":
                firefox_driver = FirefoxService(executable_path=GeckoDriverManager().install())
                self.driver = webdriver.Firefox(service=firefox_driver)
            elif browser == "safari":
                self.driver = webdriver.Safari()
            else:
                raise Exception("Browser não suportado!")
            self.driver.implicitly_wait(2)

    def close(self):
        self.driver.quit()

    def is_page(self, url, title=None):
        is_url = self.driver.current_url == url

        if title:
            element_class_title = self.driver.find_element(By.CLASS_NAME, self.class_name_title)
            is_title = element_class_title.text.lower() == title.lower()
            return is_url and is_title
        else:
            return is_url

    # def get_balance_value(self):
    #     return self.driver.find_element(By.XPATH, self.balance_value).text
