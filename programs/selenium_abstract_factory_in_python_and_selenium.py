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


class ChromeFamily:
    def create_browser(self):
        return create_driver()
    def create_reporter(self):
        return lambda result: "Chrome family: " + result

class FirefoxFamily:
    def create_browser(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        return webdriver.Firefox(options=options)
    def create_reporter(self):
        return lambda result: "Firefox family: " + result

def main():
    families = {"chrome": ChromeFamily, "firefox": FirefoxFamily}
    name = os.getenv("WAY2PYTHON_BROWSER", "chrome").lower()
    if name not in families:
        raise ValueError("Choose chrome or firefox")
    factory = families[name]()
    with browser_session(factory.create_browser) as driver:
        login(driver)
        result = wait_text(driver, "#login-status", "Welcome, learner!")
        assert result == "Welcome, learner!"
        assert factory.create_reporter()(result).startswith(name.title() + " family:")
    print('Compatible browser and reporter family passed')

if __name__ == "__main__":
    main()
