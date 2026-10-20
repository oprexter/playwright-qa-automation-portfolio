from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page, login_url: str = "/"):
        self.page = page
        self.login_url = login_url

        # Locators (preference: role > label > placeholder > text > test id)
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.get_by_test_id("error")  # no role/label; text is dynamic

    # Actions
    def open(self):
        self.page.goto(self.login_url)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    # Assertions
    def expect_loaded(self):
        expect(self.login_button).to_be_visible()

    def expect_error_contains(self, text: str):
        expect(self.error_message).to_contain_text(text)