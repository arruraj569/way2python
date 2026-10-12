class Page:
    def __init__(self, browser): self.browser = browser

shared_browser = object()
first, second = Page(shared_browser), Page(shared_browser)
print(first is second)
print(first.browser is second.browser)
