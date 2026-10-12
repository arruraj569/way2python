class Browser:
    def __init__(self, family):
        self.family = family

class Reporter:
    def __init__(self, family):
        self.family = family
    def describe(self, browser):
        if browser.family != self.family:
            raise ValueError("mixed families")
        return self.family + " browser + reporter"

class EnvironmentFactory:
    def __init__(self, family):
        self.family = family
    def browser(self):
        return Browser(self.family)
    def reporter(self):
        return Reporter(self.family)

for family in ["local", "grid"]:
    factory = EnvironmentFactory(family)
    print(factory.reporter().describe(factory.browser()))
print("Both collaborators come from one factory.")
