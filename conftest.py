import json
from pathlib import Path

import pytest

from pages.Inventory_page import InventoryPage
from pages.login_page import LoginPage

CONFIG_FILE = Path(__file__).parent / "config.json"


@pytest.fixture(scope="session")
def config():
    """Load values from config.json (root folder)."""
    with open(CONFIG_FILE, encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session", autouse=True)
def set_test_id_attribute(playwright):
    """This app uses data-test instead of Playwright's default data-testid."""
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, config):
    """Gives the built-in `page` fixture the base_url from config.json."""
    return {**browser_context_args, "base_url": config["base_url"]}


@pytest.fixture(scope="session")
def logged_in_page(browser, config):
    """Login once before all tests, logout once after all tests finish."""
    context = browser.new_context(base_url=config["base_url"])
    page = context.new_page()

    login_page = LoginPage(page, config["login_url"])
    inventory_page = InventoryPage(page)

    # ---- LOGIN (runs once at start) ----
    login_page.open()
    login_page.login(config["username"], config["password"])
    inventory_page.expect_loaded()

    yield page  # ---- all tests that use this fixture run here ----

    # ---- LOGOUT (runs once after the last test) ----
    try:
        inventory_page.logout()
        login_page.expect_loaded()
    finally:
        context.close()