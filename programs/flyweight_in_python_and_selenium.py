from dataclasses import dataclass

@dataclass(frozen=True)
class LocatorSpec:
    by: str
    value: str

class LocatorPool:
    def __init__(self):
        self.cache = {}
    def get(self, by, value):
        key = (by, value)
        if key not in self.cache:
            self.cache[key] = LocatorSpec(by, value)
        return self.cache[key]

pool = LocatorPool()
first, second = pool.get("id", "email"), pool.get("id", "email")
print(first is second)
print(first.value)
