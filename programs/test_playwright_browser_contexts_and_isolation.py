from playwright.sync_api import Page, expect

def test_practice(page: Page, base_url):
    page.goto(f"{base_url}/practice.html")
    with page.context.browser.new_context() as other_context:
        other_page = other_context.new_page()
        other_page.goto(f"{base_url}/practice.html")
        expect(other_page.get_by_test_id("login-status")).to_have_text("Not signed in")
    expect(page.get_by_test_id("login-status")).to_have_text("Not signed in")
