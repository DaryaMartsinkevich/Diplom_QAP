from selenium.webdriver.common.by import By
from tests.ui.pages.base_page import BasePage


class EditPage(BasePage):
    HEADER = (By.CLASS_NAME, 'card-header')
    EDIT_TITLE = (By.ID, 'title')
    DESCRIPTION_TITLE = (By.ID, 'description')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[data-testid="submit-button"]')
    COMPLETED_CHECKBOX = (By.CSS_SELECTOR, '[data-testid="completed-checkbox"]')
    CANCEL_BUTTON = (By.CSS_SELECTOR, '[data-testid="cancel-button"]')

    def get_header_text(self):
        return self.find_element(self.HEADER).text

    def edit_title(self, title):
        self.input_text(self.EDIT_TITLE, title)

    def edit_description(self, description):
        self.input_text(self.DESCRIPTION_TITLE, description)

    def edit_status(self):
        self.click(self.COMPLETED_CHECKBOX)

    def click_submit_button(self):
        self.click(self.SUBMIT_BUTTON)
        self.driver.save_screenshot("edit_task.png")

    def click_cancel_button(self):
        self.click(self.CANCEL_BUTTON)

    def clear_title(self):
        self.find_element(self.EDIT_TITLE).clear()

    def clear_description(self):
        self.find_element(self.DESCRIPTION_TITLE).clear()

