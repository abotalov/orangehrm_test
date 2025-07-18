from playwright.sync_api import expect

from common import models
from pages.base_page import BasePage


class EmployeeDetailsPage(BasePage):
    def expect_employee_details(self, employee: models.Employee) -> None:
        """Check if the employee details are displayed."""
        expect(
            self.page.get_by_role("heading", name=employee.full_name)
        ).to_be_visible()
