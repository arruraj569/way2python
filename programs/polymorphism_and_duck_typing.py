class ConsoleReporter:
    def write(self, message):
        print(message)
class MemoryReporter:
    def __init__(self):
        self.messages = []
    def write(self, message):
        self.messages.append(message)

def report(reporter):
    reporter.write("login passed")
report(ConsoleReporter())
