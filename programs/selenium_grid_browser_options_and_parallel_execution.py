import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
grid_url = os.getenv("SELENIUM_GRID_URL")
driver = (webdriver.Remote(command_executor=grid_url, options=options)
          if grid_url else webdriver.Chrome(options=options))
try:
    base_url = os.getenv("WAY2PYTHON_URL", "http://localhost:8080/way2python")
    driver.get(f"{base_url}/practice.html")
    heading = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
    assert heading.text == "A small lab. Real browser skills."
    print("Browser check passed")
finally:
    driver.quit()
