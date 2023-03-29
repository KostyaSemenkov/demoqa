from pages.base_page import BasePage
from components.components import WebElement


class TextBox(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'

        super().__init__(driver, self.base_url)
        self.pageData={
        'title': 'DEMOQA'

        }
        self.icon = WebElement(driver, '#app > header >a')
        # self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        # self.text_footer = WebElement(driver, '#app > footer > span')
        self.first_pole = WebElement(driver, '#userName')

