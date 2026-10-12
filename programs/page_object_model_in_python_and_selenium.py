class DriverDouble:
    def __init__(self):
        self.fields = {}
    def fill(self, name, value):
        self.fields[name] = value
    def submit(self):
        return self.fields == {"email": "learner@example.test", "password": "python123"}

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    def login(self, email, password):
        self.driver.fill("email", email)
        self.driver.fill("password", password)
        return self.driver.submit()

page = LoginPage(DriverDouble())
result = page.login("learner@example.test", "python123")
assert result is True
print("Driver double: login passed")
