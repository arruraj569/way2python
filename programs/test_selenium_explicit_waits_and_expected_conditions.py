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
    driver.find_element(By.ID, "load-message").click()
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(
        (By.ID, "async-result"), "Ready for testing"))
    assert driver.find_element(By.ID, "async-result").text == "Ready for testing"
