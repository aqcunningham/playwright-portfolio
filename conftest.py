"""
Shared fixtures for the test suite.

A fixture handles setup (before a test runs) and teardown (after it finishes)
so individual test files don't repeat browser-launch boilerplate.
"""

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    """
    Provides a fresh browser page to each test function.
    'yield' hands control to the test; code after yield runs as cleanup,
    even if the test fails.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=0)
        context = browser.new_context()
        page = context.new_page()

        yield page  # test runs here

        context.close()
        browser.close()
