class Suite:
    def __init__(self, name):
        self.name = name
        self.tests = []
    def add(self, test):
        self.tests.append(test)

smoke, full = Suite("smoke"), Suite("full")
smoke.add("login")
print(smoke.tests, full.tests)
