import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver): self.driver = driver
    def sign_in(self, email, password):
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-form button[type=submit]").click()

@pytest.fixture
def driver():
    instance = webdriver.Chrome()
    try: yield instance
    finally: instance.quit()

def test_page_object_login(driver):
    driver.get("http://localhost:8080/way2python/practice.html")
    LoginPage(driver).sign_in("learner@example.test", "python123")
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.ID, "login-status"), "Welcome, learner!"))
    assert driver.find_element(By.ID, "login-status").text == "Welcome, learner!"
