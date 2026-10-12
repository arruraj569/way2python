from playwright.sync_api import Page, expect

def test_practice(page: Page, base_url):
    page.goto(f"{base_url}/practice.html")
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Reset tasks", exact=True).click()
    with page.expect_popup() as popup_info:
        page.get_by_role("button", name="Open practice window", exact=True).click()
    popup = popup_info.value
    expect(popup.get_by_role("heading", name="Practice window", exact=True)).to_be_visible()
    popup.close()
