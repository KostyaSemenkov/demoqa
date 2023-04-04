from pages.base_page import BasePage
from components.components import WebElement


class Alerts(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'

        super().__init__(driver, self.base_url)
        self.pageData={
        'title': 'DEMOQA'

        }
        self.btn_alert = WebElement(driver, '#alertButton')
        self.confirm_btn =WebElement(driver, '#confirmButton')
        self.block = WebElement(driver, '#confirmResult')
        self.promt = WebElement(driver, '#promtButton')
        self.name = WebElement(driver, '#promptResult')