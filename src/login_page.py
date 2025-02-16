from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

        self.username_input = (By.CSS_SELECTOR, "[data-testid='login-user-id']")
        self.password_input = (By.CSS_SELECTOR, "[data-testid='login-password']")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        # Wait for username field to be present
        username_field = self.wait.until(EC.presence_of_element_located(self.username_input))
        username_field.send_keys(username)

        # Wait for password field to be present
        password_field = self.wait.until(EC.presence_of_element_located(self.password_input))
        password_field.send_keys(password)

        # Wait for login button to be clickable and click
        login_btn = self.wait.until(EC.element_to_be_clickable(self.login_button))
        login_btn.click()
