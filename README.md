# Playwright Test Automation Portfolio

Automated UI test suite built with **Playwright + pytest**, demonstrating locator strategy,
page object structure, fixtures, and CI integration.

## What this covers
- [ ] Locator strategy (role-based, text-based, CSS/XPath fallback)
- [ ] Page Object Model — one class per page, tests stay thin
- [ ] Pytest fixtures for setup/teardown (browser, page lifecycle)
- [ ] Assertions with Playwright's web-first `expect()`
- [ ] CI — tests run automatically on every push (GitHub Actions)

## Target site
Testing against: `[fill in — e.g. https://www.saucedemo.com]`

## Tech stack
- Python 3.13
- Playwright (sync API)
- pytest + pytest-playwright

## Setup
```bash
pipenv install
pipenv shell
playwright install chromium
```

## Running the tests
```bash
pytest
pytest -v                    # verbose
pytest --headed               # watch the browser while it runs
pytest tests/test_login.py    # run one file
```

## Project structure
```
playwright-portfolio/
├── tests/          # test files — what gets asserted
├── pages/          # Page Object Model — how to interact with each page
├── conftest.py      # shared pytest fixtures (browser/page setup)
├── pytest.ini        # pytest config
└── .github/workflows/tests.yml   # CI — runs the suite on every push
```

## Sample run
`[screenshot or short GIF of a passing test run goes here]`

## Author
Built by Aselle Cunningham as part of ongoing Playwright/QA automation study.
