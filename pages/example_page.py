"""
Page Object Model (POM) template.

Idea: one class per page. The class owns *how* to find and interact with
elements on that page. Test files then read like plain English, without
locator strings scattered through them — and if the site's markup changes,
you only update it here, not in every test that touches this page.
"""


class ExamplePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://example.com"

        # Locators defined once, reused by every method below
        self.heading = page.get_by_role("heading", name="Example Domain")
        self.more_info_link = page.get_by_role("link", name="More information...")

    def goto(self):
        self.page.goto(self.url)

    def click_more_info(self):
        self.more_info_link.click()
