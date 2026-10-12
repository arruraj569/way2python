class LoginService:
    def sign_in(self):
        return "Welcome, learner!"

class ProfileService:
    def save(self, name):
        return "Profile saved: " + name

class OnboardingFacade:
    def __init__(self, login, profile):
        self.login, self.profile = login, profile
    def prepare(self, name):
        return self.login.sign_in(), self.profile.save(name)

welcome, saved = OnboardingFacade(LoginService(), ProfileService()).prepare("Mira")
print(welcome)
print(saved)
