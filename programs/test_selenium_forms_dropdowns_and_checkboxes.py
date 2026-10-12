import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

@pytest.fixture
def driver():
    instance = webdriver.Chrome()
    yield instance
    instance.quit()

def test_practice(driver):
    base_url = os.getenv("WAY2PYTHON_URL", "http://localhost:8080/way2python")
    driver.get(f"{base_url}/practice.html")
    field = driver.find_element(By.ID, "display-name")
    field.clear()
    field.send_keys("Mira")
    Select(driver.find_element(By.ID, "track-select")).select_by_value("api")
    checkbox = driver.find_element(By.ID, "email-updates")
    if not checkbox.is_selected():
        checkbox.click()
    driver.find_element(By.ID, "save-profile").click()
    assert driver.find_element(By.ID, "profile-status").text == "Profile saved: Mira · API testing · updates on"
