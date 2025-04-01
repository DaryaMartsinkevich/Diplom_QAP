from selenium.webdriver.common.by import By

from tests.ui.pages.base_page import BasePage
from tests.ui.settings import url


class RegisterPage(BasePage):
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    RESISTER_BUTTON = (By.CSS_SELECTOR, '[data-testid="register-button"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-testid="login-link"]')
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, '[data-testid="flash-message-success"]')
    MESSAGE_DANGER = (By.CSS_SELECTOR, '[data-testid="flash-message-danger"]')

    "Пароль должен содержать не менее 6 символов"
    "Имя пользователя обязательно"
    "Пароль обязателен"

    def get_register_page(self):
        self.open_page(f"{url}/register")

    def enter_username(self, username):
        self.input_text(self.USERNAME, username)

    def enter_password(self, password):
        self.input_text(self.PASSWORD, password)

    def click_register(self):
        self.click(self.RESISTER_BUTTON)

    def go_to_login_page(self):
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.find_element(self.MESSAGE_DANGER).text

    def get_success_message(self):
        return self.find_element(self.MESSAGE_SUCCESS).text

    @staticmethod
    def user_not_exists(conn, username):
        cur = conn.cursor()
        cur.execute(
            'SELECT COUNT(*) from "user" WHERE username =%s',(username,)
        )
        return cur.fetchone()[0] == 0

    def valid_user(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_register()