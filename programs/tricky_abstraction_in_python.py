from abc import ABC, abstractmethod
class Reporter(ABC):
    @abstractmethod
    def write(self, message): pass
class PartialReporter(Reporter):
    pass

try:
    PartialReporter()
except TypeError:
    print("abstract method still missing")
