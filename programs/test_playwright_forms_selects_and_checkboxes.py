from playwright.sync_api import Page, expect

def test_practice(page: Page, base_url):
    page.goto(f"{base_url}/practice.html")
    page.get_by_label("Display name").fill("Mira")
    page.get_by_label("Learning track").select_option("api")
    page.get_by_label("Email updates").check()
    page.get_by_role("button", name="Save profile", exact=True).click()
    expect(page.get_by_test_id("profile-status")).to_have_text("Profile saved: Mira · API testing · updates on")
