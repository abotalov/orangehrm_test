from common import models
from pages.base_page import BasePage


class AddEmployeePage(BasePage):
    def navigate(self):
        """Navigate to the add employee page."""
        self.page.goto(f"{self.base_url}/web/index.php/pim/addEmployee")

    def add_employee(self, employee: models.Employee):
        """Add an employee."""
        self.page.get_by_placeholder("First Name").fill(employee.first_name)
        self.page.get_by_placeholder("Last Name").fill(employee.last_name)
        self._fill_employee_id(employee.employee_id)
        self.page.get_by_role("button", name="Save").click()

    def _fill_employee_id(self, employee_id: str):
        input_locator = self.page.locator(
            "//label[text()='Employee Id']/ancestor::div[contains(@class, 'oxd-input-group__label-wrapper')]/following-sibling::div//input"
        )
        input_locator.fill(employee_id)
