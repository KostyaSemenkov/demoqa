from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class WebElement:

    def __init__(self, driver, locator = ''):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

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

    def find_element_xpath(self): #new
        return self.driver.find_element(By.XPATH, self.locator)