from playwright.sync_api import expect
def test_first_browser_check(page, base_url):
    page.goto(f"{base_url}/practice.html")
    expect(page.get_by_role("heading", name="A small lab. Real browser skills.", exact=True)).to_be_visible()
    expect(page.get_by_test_id("login-status")).to_have_text("Not signed in")
