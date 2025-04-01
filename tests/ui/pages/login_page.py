from selenium.webdriver.common.by import By
from tests.ui.pages.base_page import BasePage
from tests.ui.settings import url


class LoginPage(BasePage):
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-testid="login-button"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[data-testid="register-link"]')
    MESSAGE = (By.CSS_SELECTOR, '[data-testid="flash-message-info"]')

    def get_login_page(self):
        self.open_page(f"{url}/login")

    def enter_username(self, username):
        self.input_text(self.USERNAME, username)

    def enter_password(self, password):
        self.input_text(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_message(self):
        return self.find_element(self.MESSAGE).text

    def go_to_register_page(self):
        self.click(self.REGISTER_BUTTON)

    def valid_user(self, name, password):
        self.get_login_page()
        self.enter_username(name)
        self.enter_password(password)
        self.click_login()