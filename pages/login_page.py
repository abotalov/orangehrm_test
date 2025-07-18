from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the OrangeHRM login page."""

    def navigate(self) -> None:
        """Navigate to the login page."""
        self.page.goto(f"{self.base_url}/web/index.php/auth/login")

    def login(self, username: str, password: str) -> None:
        """Login to the application."""
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
