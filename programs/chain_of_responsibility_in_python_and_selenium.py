class Handler:
    def __init__(self, kind, label, next_handler=None):
        self.kind, self.label, self.next = kind, label, next_handler
    def handle(self, error):
        if isinstance(error, self.kind):
            return self.label
        if self.next:
            return self.next.handle(error)
        return "unclassified"

chain = Handler(TimeoutError, "wait failure", Handler(AssertionError, "check failure"))
for error in [TimeoutError(), AssertionError(), ValueError()]:
    print(chain.handle(error))
print("The test still owns the failure.")
