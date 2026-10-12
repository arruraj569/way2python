from dataclasses import dataclass

@dataclass(frozen=True)
class LoginCase:
    email: str
    password: str
    expected: str

class CaseRepository:
    def get(self, name):
        if name == "valid":
            return LoginCase("learner@example.test", "python123", "Welcome, learner!")
        if name == "invalid":
            return LoginCase("learner@example.test", "wrong", "Invalid credentials")
        raise KeyError(name)
