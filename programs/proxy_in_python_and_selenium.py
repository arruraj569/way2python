from urllib.parse import urlsplit

class BrowserDouble:
    def get(self, url):
        return "opened " + url

class OriginProxy:
    def __init__(self, browser, allowed):
        self.browser = browser
        self.allowed = urlsplit(allowed)[:2]
    def get(self, url):
        if urlsplit(url)[:2] != self.allowed:
            raise ValueError("origin blocked")
        return self.browser.get(url)

proxy = OriginProxy(BrowserDouble(), "http://localhost:8080")
print(proxy.get("http://localhost:8080/way2python/practice.html"))
try:
    proxy.get("https://example.org")
except ValueError as error:
    print(error)
