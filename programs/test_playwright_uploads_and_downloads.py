from playwright.sync_api import Page, expect

def test_practice(page: Page, base_url):
    page.goto(f"{base_url}/practice.html")
    page.get_by_label("Upload a text file").set_input_files({
        "name": "sample.txt", "mimeType": "text/plain", "buffer": b"automation notes"
    })
    expect(page.get_by_test_id("file-result")).to_have_text("Loaded: sample.txt · automation notes")
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Download sample CSV", exact=True).click()
    assert download_info.value.suggested_filename == "test-results.csv"
