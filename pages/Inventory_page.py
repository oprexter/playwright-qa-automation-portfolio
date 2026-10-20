from playwright.sync_api import Page, expect
 
 
class InventoryPage:
    """Page shown right after a successful login (also holds the menu/logout)."""
 
    def __init__(self, page: Page):
        self.page = page
 
        # Locators (preference: role > label > placeholder > text > test id)
        self.title = page.get_by_test_id("title")  # plain span, no role
        self.logo = page.get_by_text("Swag Labs")
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.logout_link = page.locator("[data-test=\"logout-sidebar-link\"]")
 
    # Actions
    def logout(self):
        self.menu_button.click()
        self.logout_link.click()
 
    # Assertions
    def expect_loaded(self):
        expect(self.title).to_be_visible()
        expect(self.logo).to_be_visible()
        expect(self.menu_button).to_be_visible()
 