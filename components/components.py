from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import logging


class WebElement:

    def __init__(self, driver, locator = '', locator_type = 'css'):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type

    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    def find_elements(self):
        return self.driver.find_elements(self.get_by_type(), self.locator)

    def click(self):
        self.find_element().click()

    def check_count_elements(self, count:int):
        if len(self.find_elements()) == count:
            return True
        else:
            return False

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)

    def visible(self): # видимость
        return self.find_element().is_displayed()

    def send_keys(self, text:str): # ввести значение в поле
        self.find_element().send_keys(text)

    def click_force(self): # принудительный клик
        self.driver.execute_script("arguments[0].click();", self.find_element())

    def clear(self): # очищает поле обьекта
        self.find_element().send_keys(Keys.CONTROL + 'a')
        self.find_element().send_keys(Keys.DELETE)

    def get_dom_attribute(self, name: str): # возвращает аттрибут обьекта
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return value
        return True

    def btn_enter(self): #нажимает кнопку enter
        self.find_element().send_keys(Keys.ENTER)

    def btn_arrow_down(self): #нажимает стрелочку вниз
        self.find_element().send_keys(Keys.ARROW_DOWN)

    def get_by_type(self):
        if self.locator_type == 'id':
            return By.ID
        elif self.locator_type == 'name':
            return By.NAME
        elif self.locator_type == 'xpath':
            return By.XPATH
        elif self.locator_type == 'css':
            return By.CSS_SELECTOR
        elif self.locator_type == 'class':
            return By.CLASS_NAME
        elif self.locator_type == 'link':
            return By.LINK_TEXT
        else:
            print('locator type' + self.locator_type + 'not correct')
            return False

    def scroll_to_element(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);', self.find_element())

    def btn_escape(self):
        self.find_element().send_keys(Keys.ESCAPE)

    def check_css(self, style, value=''):
        try:
            self.driver.execute_script(f"arguments[0].style.{style} ='{value}';", self.find_element())
        except Exception as ex:
            logging.log(1, ex)
            return False
        return True