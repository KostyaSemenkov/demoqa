from pages.base_page import BasePage
from components.components import WebElement


class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'

        super().__init__(driver, self.base_url)
        self.pageData={
        'title': 'DEMOQA'

        }
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.telefon = WebElement(driver, '#userNumber')
        self.sex = WebElement(driver, '#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label')


