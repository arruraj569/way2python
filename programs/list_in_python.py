browsers = ["chromium", "firefox"]
browsers.append("webkit")
copy = browsers.copy()
copy.remove("firefox")
print(browsers)
print(copy)
