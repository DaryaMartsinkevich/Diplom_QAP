from selenium.webdriver.common.by import By
from tests.ui.pages.base_page import BasePage


# Страница просмотрка информации задач
class ViewTAsk(BasePage):
    TASK_TITLE = (By.CSS_SELECTOR, '[data-testid="task-title"]')
    TASK_DESCRIPTION = (By.CSS_SELECTOR, '[data-testid="task-description"]')
    TASK_STATUS = (By.CSS_SELECTOR, '[data-testid="task-status"]')
    TOGGLE_STATUS = (By.CSS_SELECTOR, '[data-testid="toggle-status-button"]')
    EDIT_BUTTON = (By.CSS_SELECTOR, '[data-testid="edit-button"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, '[data-testid="delete-button"]')
    BACK_BUTTON = (By.CSS_SELECTOR, '[data-testid="back-button"]')

    def get_title(self):
        return self.find_element(self.TASK_TITLE).text

    def description(self):
        return self.find_element(self.TASK_DESCRIPTION).text

    def get_status(self):
        return self.find_element(self.TASK_STATUS).text

    def toggle_status(self):
        self.click(self.TOGGLE_STATUS)

    def edit_task(self):
        self.click(self.EDIT_BUTTON)

    def delete_task(self):
        self.click(self.DELETE_BUTTON)

    def back_to_my_task(self):
        self.click(self.BACK_BUTTON)