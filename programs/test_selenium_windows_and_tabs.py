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
    original = driver.current_window_handle
    before = set(driver.window_handles)
    driver.find_element(By.ID, "open-window").click()
    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
    new_handle = (set(driver.window_handles) - before).pop()
    driver.switch_to.window(new_handle)
    assert driver.find_element(By.TAG_NAME, "h1").text == "Practice window"
    driver.close()
    driver.switch_to.window(original)
