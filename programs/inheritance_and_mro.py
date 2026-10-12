class BasePage:
    def label(self):
        return "base"
class LoginPage(BasePage):
    def label(self):
        return "login"

print(LoginPage().label())
print([cls.__name__ for cls in LoginPage.__mro__])
