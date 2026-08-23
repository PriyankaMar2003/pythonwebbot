import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def run_bot():
    # 1. Configure headless Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")

    # Selenium 4+ automatically manages the driver executable
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    print("🚀 Starting Web Testing Bot...\n")

    try:
        # Test Case 1: Load Page
        print("1. Navigating to SauceDemo login page...")
        driver.get("https://www.saucedemo.com/")
        assert "Swag Labs" in driver.title, "Page title does not match."
        print("   [PASS] Page loaded successfully.")

        # Test Case 2: Perform Login
        print("2. Entering user credentials...")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Test Case 3: Verify Inventory Dashboard
        print("3. Verifying dashboard access...")
        inventory = driver.find_element(By.ID, "inventory_container")
        assert inventory.is_displayed(), "Inventory container was not found."
        
        page_title = driver.find_element(By.CLASS_NAME, "title").text
        assert page_title == "Products", f"Expected 'Products', got '{page_title}'."
        print("   [PASS] Login successful and dashboard loaded.")

        # Test Case 4: Add Item to Cart
        print("4. Testing 'Add to Cart' functionality...")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart_badge == "1", f"Expected 1 item in cart, found '{cart_badge}'."
        print("   [PASS] Item added to cart successfully.")

        print("\n✅ All automated tests completed without errors.")

    except AssertionError as error:
        print(f"\n❌ Test Assertion Failed: {error}")
        sys.exit(1)
    except Exception as error:
        print(f"\n❌ Unexpected Error Occurred: {error}")
        sys.exit(1)
    finally:
        driver.quit()
        print("🧹 Browser closed.")


if __name__ == "__main__":
    run_bot()
