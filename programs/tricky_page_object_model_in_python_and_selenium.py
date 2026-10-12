class Page:
    def login(self):
        return "Welcome"

page = Page()
print(callable(page.login))
print(page.login())
