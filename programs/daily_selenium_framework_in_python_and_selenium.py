from contextlib import contextmanager

class DriverDouble:
    def __init__(self):
        self.status = "Not signed in"
    def quit(self):
        print("driver double quit")

def create_driver():
    return DriverDouble()

@contextmanager
def browser():
    driver = create_driver()
    try:
        yield driver
    finally:
        driver.quit()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    def login(self, email, password):
        self.driver.status = "Welcome, learner!" if (email, password) == ("learner@example.test", "python123") else "Invalid credentials"
        return self.driver.status

case = {"email": "learner@example.test", "password": "python123"}
with browser() as driver:
    assert LoginPage(driver).login(**case) == "Welcome, learner!"
    print("daily smoke passed with a driver double")
