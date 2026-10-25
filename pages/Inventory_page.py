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
        self.product_count = page.locator("[data-test='inventory-item']").count()
        self.product = page.locator("[data-test='inventory-item']")
 
    # Actions
    def logout(self):
        self.menu_button.click()
        self.logout_link.click()
 
    # Assertions
    def expect_loaded(self):
        expect(self.title).to_be_visible()
        expect(self.logo).to_be_visible()
        expect(self.menu_button).to_be_visible()

    def assert_product_count(self, expected_count):
        assert self.product_count == expected_count


    def assert_product_details(self):
        products = self.product

        for i in range(products.count()):
            product = products.nth(i)

            assert product.locator("[data-test='inventory-item-name']").inner_text().strip()
            assert product.locator("[data-test='inventory-item-desc']").inner_text().strip()
            assert product.locator("[data-test='inventory-item-price']").inner_text().strip()
            assert product.locator("img.inventory_item_img").is_visible() 
            
    def assert_sort_by_name_ascending(self):
        self.page.locator("[data-test='product-sort-container']").select_option("az")

        product_names = self.page.locator(
            "[data-test='inventory-item-name']"
        ).all_inner_texts()

        expected_names = sorted(product_names)

        if product_names == expected_names:
            print("Products sorted A to Z successfully")

        assert product_names == expected_names, (
            f"Products are not sorted A to Z.\n"
            f"Actual order: {product_names}\n"
            f"Expected order: {expected_names}"
        )

    def assert_sort_by_name_descending(self):
        self.page.locator("[data-test='product-sort-container']").select_option("za")

        product_names = self.page.locator(
            "[data-test='inventory-item-name']"
        ).all_inner_texts()

        expected_names = sorted(product_names, reverse=True)            

        if product_names == expected_names:
            print("Products sorted Z to A successfully")

        assert product_names == expected_names, (
            f"Products are not sorted Z to A.\n"
            f"Actual order: {product_names}\n"
            f"Expected order: {expected_names}"
        )


    def assert_sort_by_price_low_to_high(self):
        # Step 1: Select Price Low to High
        self.page.locator("[data-test='product-sort-container']").select_option("lohi")

        # Step 2: Get all product prices
        product_prices = self.page.locator("[data-test='inventory-item-price']").all_inner_texts()

        # Step 3: Convert prices from strings to numbers
        actual_prices = []

        for price in product_prices:
            price = price.replace("$", "").strip()
            price = float(price)
            actual_prices.append(price)

        # Step 4: Sort prices in ascending order
        expected_prices = sorted(actual_prices)

        # Step 5: Assert that the actual order matches
        # the expected ascending order
        assert actual_prices == expected_prices, (
            f"Products are not sorted by price low to high.\n"
            f"Actual prices: {actual_prices}\n"
            f"Expected prices: {expected_prices}"
        )

    def assert_sort_by_price_high_to_low(self):

        # Step 1: Select Price High to Low
        self.page.locator("[data-test='product-sort-container']").select_option("hilo")

        # Step 2: Get all product prices
        product_prices = self.page.locator("[data-test='inventory-item-price']").all_inner_texts()

        # Step 3: Convert prices into numbers
        actual_prices = []

        for price in product_prices:
            price = price.replace("$", "").strip()
            price = float(price)
            actual_prices.append(price)

        # Step 4: Sort prices in descending order
        expected_prices = sorted(actual_prices, reverse=True)

        # Step 5: Verify the sorting
        assert actual_prices == expected_prices, (
            f"Products are not sorted by price high to low.\n"
            f"Actual prices: {actual_prices}\n"
            f"Expected prices: {expected_prices}"
        )