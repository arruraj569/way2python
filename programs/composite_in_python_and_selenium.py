class Check:
    def __init__(self, result):
        self.result = result
    def evaluate(self):
        return self.result

class Suite:
    def __init__(self, children):
        self.children = list(children)
    def evaluate(self):
        return bool(self.children) and all(child.evaluate() for child in self.children)

smoke = Suite([Check(True), Suite([Check(True), Check(False)])])
print(smoke.evaluate())
print(Suite([]).evaluate())
