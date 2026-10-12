shared_locator = ("id", "email")
test_a = {"locator": shared_locator, "text": "a@example.test"}
test_b = {"locator": shared_locator, "text": "b@example.test"}
test_a["text"] = "changed"
print(test_b["text"])
print(test_a["locator"] is test_b["locator"])
