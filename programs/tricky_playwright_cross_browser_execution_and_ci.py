browsers = ["chromium", "firefox", "webkit"]
tests = ["login", "profile"]
matrix = [(browser, test) for browser in browsers for test in tests]
print(len(matrix))
print(len(set(matrix)))
