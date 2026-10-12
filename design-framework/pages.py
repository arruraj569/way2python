from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components import ProfileComponent

class PracticePage:
    def __init__(self, driver):
        self.driver = driver
        self.profile = ProfileComponent(driver)
        self.control("email")
    def control(self, identity):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, identity)))
    def sign_in(self, email, password):
        for identity, value in [("email", email), ("password", password)]:
            element = self.control(identity)
            element.clear()
            element.send_keys(value)
        self.driver.find_element(By.CSS_SELECTOR, "#login-form button[type=submit]").click()
    def login_status(self, expected):
        WebDriverWait(self.driver, 5).until(
            lambda browser: browser.find_element(By.ID, "login-status").text == expected)
        return self.driver.find_element(By.ID, "login-status").text
