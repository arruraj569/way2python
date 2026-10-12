from playwright.sync_api import Page, expect

def test_practice(page: Page, base_url):
    page.goto(f"{base_url}/practice.html")
    page.get_by_label("Task name").fill("API smoke checks")
    page.get_by_role("button", name="Add task", exact=True).click()
    row = page.get_by_role("row").filter(has_text="API smoke checks")
    expect(row).to_be_visible()
    row.get_by_role("checkbox").check()
    expect(page.get_by_test_id("task-summary")).to_have_text("1 of 1 tasks complete")
