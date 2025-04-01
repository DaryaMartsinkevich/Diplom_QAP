import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def get_element(self, selector):
        return self.driver.find_element(*selector)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def click(self, selector):
        element = self.driver.find_element(*selector)
        element.click()

    def input_text(self, selector, text):
        element = self.driver.find_element(*selector)
        element.send_keys(text)

    def fill(self, selector, text):
        self.get_element(selector).send_keys(text)

    def save_screenshot(self, name):
        self.driver.save_screenshot(name)



