from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.ui.pages.base_page import BasePage


class TaskPage(BasePage):
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '[data-testid="flash-message-success"]')
    CREATE_TASK = (By.CSS_SELECTOR, '[data-testid="create-task-button"]')
    CREATE_FIRST_TASK = (By.CSS_SELECTOR, '[data-testid="create-first-task-link"]')
    NO_TASK_MESSAGE = (By.CSS_SELECTOR, '[data-testid="no-tasks-message"]')
    MY_TASK = (By.CSS_SELECTOR, '[data-testid="nav-tasks"]')
    TASK_TITLE = (By.CSS_SELECTOR, ['data-testid="task-title-3"'])
    VIEW_TASK = (By.CLASS_NAME, 'btn btn-sm btn-info')
    EDIT_TASK = (By.XPATH, '/html/body/div/div[3]/div[1]/div/div[3]/a[2]')
    DELETE_TASK = (By.XPATH, '/html/body/div/div[3]/div[1]/div/div[3]/button')
    DELETE_MODAL_CONTENT = (By.CSS_SELECTOR, '.modal-content')
    DELETE_CONFIRM_BUTTON = (By.CSS_SELECTOR, '[data-testid^="delete-confirm-button"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '[data-testid="nav-logout"]')

    def get_success_message(self):
        return self.find_element(self.SUCCESS_MESSAGE).text

    def creat_task(self):
        self.click(self.CREATE_TASK)

    def view_task(self):
        self.click(self.VIEW_TASK)

    def edit_task(self):
        self.click(self.EDIT_TASK)

    def delete_task(self):
        self.click(self.DELETE_TASK)

    def delete_button_confirm(self):
        modal = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.DELETE_MODAL_CONTENT)
        )

        confirm_button = modal.find_element(*self.DELETE_CONFIRM_BUTTON)
        confirm_button.click()
        self.driver.save_screenshot("delete.png")
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.DELETE_MODAL_CONTENT)
        )

    def logout(self):
        self.click(self.LOGOUT_BUTTON)
        self.driver.save_screenshot("logout.png")



