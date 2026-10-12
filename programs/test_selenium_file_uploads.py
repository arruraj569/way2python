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
    from pathlib import Path
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as folder:
        sample = Path(folder) / "sample.txt"
        sample.write_text("automation notes", encoding="utf-8")
        driver.find_element(By.ID, "sample-file").send_keys(str(sample.resolve()))
        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.ID, "file-result"), "automation notes"))
        assert driver.find_element(By.ID, "file-result").text == "Loaded: sample.txt · automation notes"
