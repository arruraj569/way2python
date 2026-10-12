from playwright.sync_api import expect
class LoginPage:
    def __init__(self, page):
        self.page = page
    def sign_in(self, email, password):
        self.page.get_by_label("Email", exact=True).fill(email)
        self.page.get_by_label("Password", exact=True).fill(password)
        self.page.get_by_role("button", name="Sign in", exact=True).click()

def test_login(page, base_url):
    page.goto(f"{base_url}/practice.html")
    LoginPage(page).sign_in("learner@example.test", "python123")
    expect(page.get_by_test_id("login-status")).to_have_text("Welcome, learner!")
