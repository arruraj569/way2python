from dataclasses import dataclass

@dataclass(frozen=True)
class Profile:
    name: str
    track: str

class ProfileBuilder:
    def __init__(self):
        self.name, self.track = "Learner", "python"
    def named(self, name):
        self.name = name
        return self
    def learning(self, track):
        self.track = track
        return self
    def build(self):
        return Profile(self.name, self.track)

builder = ProfileBuilder().named("Mira")
first = builder.build()
second = builder.learning("selenium").build()
print(first)
print(second)
