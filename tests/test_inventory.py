from pages.Inventory_page import InventoryPage
from pages.login_page import LoginPage




def test_inv_001_product_count(logged_in_page):
    """to verify that the product count is 6"""
    
    inventory = InventoryPage(logged_in_page)
    inventory.assert_product_count(6)


def test_inv_002_verify_product_details(logged_in_page):    
    """to verify that all products have name, description, price and image"""

    inventory = InventoryPage(logged_in_page)
    inventory.assert_product_details()


def test_inv_003_sort_by_name_ascending(logged_in_page):
    """to verify that the products are sorted by name in ascending order"""

    inventory = InventoryPage(logged_in_page)
    inventory.assert_sort_by_name_ascending()

def test_inv_004_sort_by_name_descending(logged_in_page):
    """to verify that the products are sorted by name in descending order"""

    inventory = InventoryPage(logged_in_page)
    inventory.assert_sort_by_name_descending()

def test_inv_005_sort_by_price_low_to_high(logged_in_page):
    """to verify that the products are sorted by price in low to high order"""

    inventory = InventoryPage(logged_in_page)
    inventory.assert_sort_by_price_low_to_high()

def test_inv_006_sort_by_price_high_to_low(logged_in_page):
    """to verify that the products are sorted by price in high to low order"""

    inventory = InventoryPage(logged_in_page)
    inventory.assert_sort_by_price_high_to_low()