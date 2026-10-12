import os
import pytest
from driver_factory import create_driver

@pytest.fixture
def driver():
    browser = create_driver()
    try:
        url = os.getenv("WAY2PYTHON_URL", "http://localhost:8080/way2python").rstrip("/")
        browser.get(url + "/practice.html")
        yield browser
    finally:
        browser.quit()
