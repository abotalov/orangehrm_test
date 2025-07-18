import pytest

from config import ADMIN_PASSWORD, ADMIN_USERNAME
from common import factories


@pytest.fixture
def login(page, login_page, dashboard_page):
    """Login to the application."""
    login_page.navigate()
    login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
    dashboard_page.expect_logged_in()


def test_add_employee(login, add_employee_page, employee_details_page):
    employee = factories.EmployeeFactory()
    add_employee_page.navigate()
    add_employee_page.add_employee(employee)
    employee_details_page.expect_employee_details(employee)
