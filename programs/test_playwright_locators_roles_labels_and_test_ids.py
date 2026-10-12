from playwright.sync_api import Page, expect

def test_practice(page: Page, base_url):
    page.goto(f"{base_url}/practice.html")
    page.get_by_label("Email", exact=True).fill("learner@example.test")
    page.get_by_label("Password", exact=True).fill("python123")
    page.get_by_role("button", name="Sign in", exact=True).click()
    expect(page.get_by_test_id("login-status")).to_have_text("Welcome, learner!")
