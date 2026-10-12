from playwright.sync_api import Page, expect

def test_practice(page: Page, base_url):
    page.goto(f"{base_url}/practice.html")
    page.route("**/frame.html", lambda route: route.fulfill(
        status=200, content_type="text/html",
        body='<main><h1>Mocked frame</h1></main>'
    ))
    page.reload()
    expect(page.frame_locator("#practice-frame").get_by_role("heading")).to_have_text("Mocked frame")
