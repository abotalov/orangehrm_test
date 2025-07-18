from playwright.sync_api import expect

from pages.base_page import BasePage


class DashboardPage(BasePage):
    def expect_logged_in(self) -> None:
        """Check if the user is logged in."""
        expect(self.page.get_by_role("heading", name="Dashboard")).to_be_visible()
