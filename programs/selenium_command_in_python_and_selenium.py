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


class FillCommand:
    def __init__(self, driver, selector, value):
        self.driver, self.selector, self.value = driver, selector, value
    def execute(self):
        fill(self.driver, self.selector, self.value)

class ClickCommand:
    def __init__(self, driver, selector):
        self.driver, self.selector = driver, selector
    def execute(self):
        control(self.driver, self.selector).click()

def main():
    with browser_session() as driver:
        commands = [FillCommand(driver, "#display-name", "Mira"), ClickCommand(driver, "#save-profile")]
        for command in commands:
            command.execute()
        assert wait_text(driver, "#profile-status", "Profile saved: Mira · Python basics · updates off") == "Profile saved: Mira · Python basics · updates off"
    print('Form command sequence passed')

if __name__ == "__main__":
    main()
