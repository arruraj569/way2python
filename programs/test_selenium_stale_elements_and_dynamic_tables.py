import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    instance = webdriver.Chrome()
    yield instance
    instance.quit()

def test_practice(driver):
    base_url = os.getenv("WAY2PYTHON_URL", "http://localhost:8080/way2python")
    driver.get(f"{base_url}/practice.html")
    driver.find_element(By.ID, "task-name").send_keys("API checks")
    driver.find_element(By.ID, "add-task").click()
    row = driver.find_element(By.XPATH, "//tr[td[normalize-space()='API checks']]")
    row.find_element(By.CSS_SELECTOR, "input[type=checkbox]").click()
    assert driver.find_element(By.ID, "task-summary").text == "1 of 1 tasks complete"
