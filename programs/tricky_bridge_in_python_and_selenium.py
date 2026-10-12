class Reporter:
    def write(self, text):
        return text.upper()

def journey(reporter):
    return reporter.write("login")

print(journey(Reporter()))
