import pytest

from playwright.sync_api import Page, expect

from config import TIMEOUT_SECONDS
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.pim.add_employee_page import AddEmployeePage
from pages.pim.employee_details_page import EmployeeDetailsPage


timeout_ms = TIMEOUT_SECONDS * 1000


expect.set_options(timeout=timeout_ms)


@pytest.fixture
def new_context(new_context):
    def _new_context_with_timeout():
        context = new_context()
        context.set_default_timeout(timeout_ms)
        return context

    return _new_context_with_timeout


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page)


@pytest.fixture
def add_employee_page(page: Page) -> AddEmployeePage:
    return AddEmployeePage(page)


@pytest.fixture
def employee_details_page(page: Page) -> EmployeeDetailsPage:
    return EmployeeDetailsPage(page)
