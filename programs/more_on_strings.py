raw = "  smoke, api, browser  "
tags = [tag.strip() for tag in raw.strip().split(",")]
print(tags)
print(" | ".join(tags))
print("test_login.py".removesuffix(".py"))
