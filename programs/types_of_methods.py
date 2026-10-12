class BrowserConfig:
    def __init__(self, name):
        self.name = name
    def label(self):
        return self.name.upper()
    @classmethod
    def default(cls):
        return cls("chromium")
    @staticmethod
    def supported(name):
        return name in {"chromium", "firefox", "webkit"}

print(BrowserConfig.default().label())
print(BrowserConfig.supported("firefox"))
