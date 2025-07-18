from playwright.sync_api import Page

from config import BASE_URL


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = BASE_URL
