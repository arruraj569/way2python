from abc import ABC, abstractmethod
class Reporter(ABC):
    @abstractmethod
    def write(self, message):
        pass
class ConsoleReporter(Reporter):
    def write(self, message):
        print(message)

ConsoleReporter().write("All checks complete")
