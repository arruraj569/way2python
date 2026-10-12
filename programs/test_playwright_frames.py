from playwright.sync_api import Page, expect

def test_practice(page: Page, base_url):
    page.goto(f"{base_url}/practice.html")
    frame = page.frame_locator("#practice-frame")
    frame.get_by_label("Frame email").fill("mira@example.test")
    frame.get_by_role("button", name="Save email", exact=True).click()
    expect(frame.get_by_role("status")).to_have_text("Saved: mira@example.test")
