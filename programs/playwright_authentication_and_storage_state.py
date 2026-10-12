from pathlib import Path
from tempfile import TemporaryDirectory
from playwright.sync_api import sync_playwright

# Demonstrate storage with a harmless cookie, not real credentials.
with TemporaryDirectory() as folder, sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    context.add_cookies([{"name": "demo_user", "value": "learner",
                          "url": "http://localhost:8080/way2python/"}])
    state_file = Path(folder) / "demo-state.json"
    context.storage_state(path=state_file)
    restored = browser.new_context(storage_state=state_file)
    cookie = next(item for item in restored.cookies() if item["name"] == "demo_user")
    print("Restored demonstration user:", cookie["value"])
    restored.close()
    context.close()
    browser.close()
