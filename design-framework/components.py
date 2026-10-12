from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class ProfileComponent:
    def __init__(self, driver):
        self.driver = driver
    def root(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "profile-form")))
    def save(self, name, track):
        field = self.root().find_element(By.ID, "display-name")
        field.clear()
        field.send_keys(name)
        Select(self.root().find_element(By.ID, "track-select")).select_by_value(track)
        self.root().find_element(By.ID, "save-profile").click()
    def status(self, expected):
        WebDriverWait(self.driver, 5).until(
            lambda browser: browser.find_element(By.ID, "profile-status").text == expected)
        return self.driver.find_element(By.ID, "profile-status").text
