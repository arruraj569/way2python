class BrowserDouble:
    def __init__(self, name):
        self.name = name

class SmokeCreator:
    def create_browser(self):
        raise NotImplementedError
    def run(self):
        browser = self.create_browser()
        return browser.name + " smoke ready"

class ChromeSmoke(SmokeCreator):
    def create_browser(self):
        return BrowserDouble("Chrome")

class FirefoxSmoke(SmokeCreator):
    def create_browser(self):
        return BrowserDouble("Firefox")

print(ChromeSmoke().run())
print(FirefoxSmoke().run())
