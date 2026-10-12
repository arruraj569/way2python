class PageObject:
    def __init__(self, page): self.page = page
page = object()
login, profile = PageObject(page), PageObject(page)
print(login.page is profile.page)
print(login is profile)
