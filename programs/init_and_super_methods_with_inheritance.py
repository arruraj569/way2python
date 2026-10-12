class BasePage:
    def __init__(self, page_name):
        self.page_name = page_name
class LoginPage(BasePage):
    def __init__(self):
        super().__init__("login")
        self.submit_label = "Sign in"

page = LoginPage()
print(page.page_name, page.submit_label)
