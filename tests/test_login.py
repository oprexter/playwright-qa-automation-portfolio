from pages.Inventory_page import InventoryPage
from pages.login_page import LoginPage
 
 
def test_valid_login_and_logout(page, config):
    login_page = LoginPage(page, config["login_url"])
    inventory_page = InventoryPage(page)
 
    login_page.open()
    login_page.login(config["username"], config["password"])
    inventory_page.expect_loaded()
 
    inventory_page.logout()
    login_page.expect_loaded()
 
 
def test_invalid_login_shows_error(page, config):
    login_page = LoginPage(page, config["login_url"])
 
    login_page.open()
    login_page.login("username", "wrong_password")
    login_page.expect_error_contains("do not match")
 