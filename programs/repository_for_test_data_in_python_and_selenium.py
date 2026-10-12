from copy import deepcopy

class CaseRepository:
    def __init__(self, cases):
        self.cases = deepcopy(cases)
    def get(self, name):
        return deepcopy(self.cases[name])

repository = CaseRepository({"valid": {"email": "learner@example.test"}})
first = repository.get("valid")
first["email"] = "edited@example.test"
print(first["email"])
print(repository.get("valid")["email"])
