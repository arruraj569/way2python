from playwright.sync_api import Page, expect

def test_practice(page: Page, base_url):
    page.goto(f"{base_url}/practice.html")
    seen = []
    page.on("response", lambda response: seen.append(response.url))
    page.reload()
    expect(page.get_by_role("heading", name="A small lab. Real browser skills.")).to_be_visible()
    assert any("practice.html" in url for url in seen)
