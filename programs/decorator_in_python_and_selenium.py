class LoginAction:
    def execute(self):
        return "Welcome, learner!"

class ReportedAction:
    def __init__(self, action):
        self.action = action
    def execute(self):
        print("login started")
        result = self.action.execute()
        print("login finished")
        return result

print(ReportedAction(LoginAction()).execute())
