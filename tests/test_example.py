"""
Example test — replace this with real tests against your chosen target site.
Demonstrates: fixture use, Page Object Model, and a basic assertion.
"""

from playwright.sync_api import expect
from pages.example_page import ExamplePage


def test_heading_is_visible(page):
    example_page = ExamplePage(page)
    example_page.goto()

    expect(example_page.heading).to_be_visible()


def test_more_info_link_navigates(page):
    example_page = ExamplePage(page)
    example_page.goto()

    example_page.click_more_info()

    expect(page).to_have_url("https://www.iana.org/help/example-domains")
