class BrokenChain:
    def named(self, name):
        self.name = name

result = BrokenChain().named("Mira")
print(result is None)
