class Actor:
    def __init__(self, name, abilities):
        self.name, self.abilities = name, abilities
    def attempts(self, task):
        task.perform_as(self)

class SignIn:
    def perform_as(self, actor):
        actor.abilities["browse"]["status"] = "Welcome, learner!"

class WelcomeText:
    def answered_by(self, actor):
        return actor.abilities["browse"]["status"]

actor = Actor("Mira", {"browse": {"status": "Not signed in"}})
actor.attempts(SignIn())
assert WelcomeText().answered_by(actor) == "Welcome, learner!"
print(actor.name, "completed the driver-double journey")
