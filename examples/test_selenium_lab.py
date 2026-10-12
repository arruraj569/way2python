"""Independent Chrome sessions; override the target with WAY2PYTHON_URL."""
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options=webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    instance=webdriver.Chrome(options=options)
    try:
        instance.get(os.getenv('WAY2PYTHON_URL','http://localhost:8080/way2python').rstrip('/')+'/practice.html')
        yield instance
    finally:
        instance.quit()

def test_login(driver):
    driver.find_element(By.ID,'email').send_keys('learner@example.test')
    driver.find_element(By.ID,'password').send_keys('python123')
    driver.find_element(By.CSS_SELECTOR,'#login-form button[type=submit]').click()
    WebDriverWait(driver,5).until(EC.text_to_be_present_in_element((By.ID,'login-status'),'Welcome, learner!'))
    assert driver.find_element(By.ID,'login-status').text == 'Welcome, learner!'

def test_profile_and_wait(driver):
    field=driver.find_element(By.ID,'display-name');field.clear();field.send_keys('Mira')
    Select(driver.find_element(By.ID,'track-select')).select_by_value('api')
    driver.find_element(By.ID,'email-updates').click()
    driver.find_element(By.ID,'save-profile').click()
    assert driver.find_element(By.ID,'profile-status').text == 'Profile saved: Mira · API testing · updates on'
    driver.find_element(By.ID,'load-message').click()
    WebDriverWait(driver,5).until(EC.text_to_be_present_in_element((By.ID,'async-result'),'Ready for testing'))

def test_tasks_and_confirm(driver):
    driver.find_element(By.ID,'task-name').send_keys('Browser checks')
    driver.find_element(By.ID,'add-task').click()
    row=driver.find_element(By.XPATH,"//tr[td[normalize-space()='Browser checks']]")
    row.find_element(By.CSS_SELECTOR,'input[type=checkbox]').click()
    assert driver.find_element(By.ID,'task-summary').text == '1 of 1 tasks complete'
    driver.find_element(By.ID,'confirm-reset').click()
    WebDriverWait(driver,5).until(EC.alert_is_present()).accept()
    assert driver.find_element(By.ID,'task-summary').text == '0 of 0 tasks complete'

def test_frame_and_new_window(driver):
    WebDriverWait(driver,5).until(EC.frame_to_be_available_and_switch_to_it((By.ID,'practice-frame')))
    driver.find_element(By.ID,'frame-email').send_keys('mira@example.test')
    driver.find_element(By.ID,'frame-save').click()
    assert driver.find_element(By.ID,'frame-status').text == 'Saved: mira@example.test'
    driver.switch_to.default_content()
    original=driver.current_window_handle;before=set(driver.window_handles)
    driver.find_element(By.ID,'open-window').click()
    WebDriverWait(driver,5).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window((set(driver.window_handles)-before).pop())
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.TAG_NAME,'h1')))
    assert driver.find_element(By.TAG_NAME,'h1').text == 'Practice window'
    driver.close();driver.switch_to.window(original)
