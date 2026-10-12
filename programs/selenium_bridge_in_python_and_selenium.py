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


class ConsoleReport:
    def format(self, journey, outcome):
        return journey + ": " + outcome

class CIReport:
    def format(self, journey, outcome):
        return "[CI] " + journey + ": " + outcome

class Journey:
    def __init__(self, driver, reporter):
        self.driver, self.reporter = driver, reporter
    def run(self):
        outcome = self.perform()
        return outcome, self.reporter.format(self.label, outcome)

class LoginJourney(Journey):
    label = "login"
    def perform(self):
        login(self.driver)
        return wait_text(self.driver, "#login-status", "Welcome, learner!")

class ProfileJourney(Journey):
    label = "profile"
    def perform(self):
        save_profile(self.driver, "Mira")
        return wait_text(self.driver, "#profile-status", "Profile saved: Mira · Selenium · updates off")

def main():
    with browser_session() as driver:
        welcome, console = LoginJourney(driver, ConsoleReport()).run()
        saved, ci = ProfileJourney(driver, CIReport()).run()
        assert welcome == "Welcome, learner!"
        assert saved == "Profile saved: Mira · Selenium · updates off"
        assert console.startswith("login:") and ci.startswith("[CI] profile:")
    print('Independent journey and reporting dimensions passed')

if __name__ == "__main__":
    main()
