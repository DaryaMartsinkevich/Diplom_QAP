from selenium.webdriver.common.by import By
from tests.ui.pages.base_page import BasePage


# Страница создания задачи
class CreateTaskPage(BasePage):
    TASK_TITLE = (By.ID, 'title')
    TASK_DESCRIPTION = (By.ID, 'description')
    TASK_BUTTON = (By.CSS_SELECTOR, '[data-testid="submit-button"]')
    CANCEL_TASK_BUTTON = (By.CSS_SELECTOR, '[data-testid="cancel-button"]')
    MY_TASK = (By.CSS_SELECTOR, '[data-testid="nav-tasks"]')
    CADR_HEADER = (By.CLASS_NAME, 'card-header')

    def enter_title(self, title):
        self.input_text(self.TASK_TITLE, title)

    def enter_description(self, description):
        self.input_text(self.TASK_DESCRIPTION, description)

    def click_submit_button(self):
        self.click(self.TASK_BUTTON)

    def get_header(self):
        return self.find_element(self.CADR_HEADER).text

