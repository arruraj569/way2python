"""Run against the local Way2Python lab with Selenium and installed Chrome."""
import os
from contextlib import contextmanager
from copy import deepcopy
from dataclasses import dataclass
from urllib.parse import urlsplit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

BASE_URL = os.getenv("WAY2PYTHON_URL", "http://localhost:8080/way2python").rstrip("/")

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    return webdriver.Chrome(options=options)

@contextmanager
def browser_session(factory=create_driver):
    driver = factory()
    try:
        driver.get(BASE_URL + "/practice.html")
        yield driver
    finally:
        driver.quit()

def control(driver, selector):
    return WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

def fill(driver, selector, value):
    field = control(driver, selector)
    field.clear()
    field.send_keys(value)

def wait_text(driver, selector, expected):
    WebDriverWait(driver, 5).until(
        lambda current: current.find_element(By.CSS_SELECTOR, selector).text == expected)
    return driver.find_element(By.CSS_SELECTOR, selector).text

def login(driver, email="learner@example.test", password="python123"):
    fill(driver, "#email", email)
    fill(driver, "#password", password)
    control(driver, "#login-form button[type=submit]").click()

def save_profile(driver, name, track="selenium"):
    fill(driver, "#display-name", name)
    Select(control(driver, "#track-select")).select_by_value(track)
    control(driver, "#save-profile").click()


class CaseRepository:
    def valid_login(self):
        return {"email": "learner@example.test", "password": "python123"}

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    def sign_in(self, email, password):
        login(self.driver, email, password)
        return wait_text(self.driver, "#login-status", "Welcome, learner!")

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
    def save(self, name):
        save_profile(self.driver, name)
        return wait_text(self.driver, "#profile-status", "Profile saved: " + name + " · Selenium · updates off")

def main():
    with browser_session() as driver:
        case = CaseRepository().valid_login()
        welcome = LoginPage(driver).sign_in(**case)
        saved = ProfilePage(driver).save("Mira")
        assert welcome == "Welcome, learner!"
        assert saved == "Profile saved: Mira · Selenium · updates off"
    print('Daily login and profile framework smoke passed')

if __name__ == "__main__":
    main()
