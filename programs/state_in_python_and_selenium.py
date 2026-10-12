class SignedOut:
    def label(self):
        return "signed out"
    def login(self, session):
        session.state = SignedIn()

class SignedIn:
    def label(self):
        return "signed in"
    def login(self, session):
        raise ValueError("already signed in")

class Session:
    def __init__(self):
        self.state = SignedOut()
    def login(self):
        self.state.login(self)

session = Session()
print(session.state.label())
session.login()
print(session.state.label())
try:
    session.login()
except ValueError as error:
    print(error)
