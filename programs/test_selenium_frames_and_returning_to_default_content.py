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
    WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "practice-frame")))
    driver.find_element(By.ID, "frame-email").send_keys("mira@example.test")
    driver.find_element(By.ID, "frame-save").click()
    assert driver.find_element(By.ID, "frame-status").text == "Saved: mira@example.test"
    driver.switch_to.default_content()
    assert driver.find_element(By.ID, "task-table").is_displayed()
