from playwright.sync_api import Page, expect

def test_practice(page: Page, base_url):
    page.goto(f"{base_url}/practice.html")
    page.get_by_role("button", name="Load message", exact=True).click()
    expect(page.get_by_test_id("async-result")).to_have_text("Ready for testing")
