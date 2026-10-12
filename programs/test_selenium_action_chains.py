import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def driver():
    instance = webdriver.Chrome()
    yield instance
    instance.quit()

def test_practice(driver):
    base_url = os.getenv("WAY2PYTHON_URL", "http://localhost:8080/way2python")
    driver.get(f"{base_url}/practice.html")
    field = driver.find_element(By.ID, "task-name")
    ActionChains(driver).move_to_element(field).click().send_keys("Browser checks").perform()
    driver.find_element(By.ID, "add-task").click()
    assert "Browser checks" in driver.find_element(By.ID, "task-table").text
