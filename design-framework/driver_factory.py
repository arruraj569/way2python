import os
from selenium import webdriver

def create_driver():
    name = os.getenv("WAY2PYTHON_BROWSER", "chrome").lower()
    if name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        return webdriver.Chrome(options=options)
    if name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        return webdriver.Firefox(options=options)
    raise ValueError("WAY2PYTHON_BROWSER must be chrome or firefox")
