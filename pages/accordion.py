from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'

        super().__init__(driver, self.base_url)
        self.pageData={
        'title': 'DEMOQA'

        }
        self.content = WebElement(driver, '#section1Content > p')
        self.header = WebElement(driver, '#section1Heading')
        self.content2 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.content3 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.content4 = WebElement(driver, '#section3Content > p')