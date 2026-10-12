from playwright.sync_api import sync_playwright
with sync_playwright() as playwright:
    client = playwright.request.new_context(base_url="http://127.0.0.1:8765",
        extra_http_headers={"Authorization": "Bearer demo-token"})
    try:
        response = client.get("/users", timeout=5000)
        assert response.status == 200
        assert isinstance(response.json()["items"], list)
        print("Playwright API check passed")
    finally:
        client.dispose()
