class ConsoleReporter:
    def write(self, message):
        return "console: " + message

class CIReporter:
    def write(self, message):
        return "ci: " + message

class Journey:
    def __init__(self, reporter):
        self.reporter = reporter
    def complete(self):
        return self.reporter.write(self.label + " passed")

class LoginJourney(Journey):
    label = "login"

class ProfileJourney(Journey):
    label = "profile"

print(LoginJourney(ConsoleReporter()).complete())
print(ProfileJourney(CIReporter()).complete())
