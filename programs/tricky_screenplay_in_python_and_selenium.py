class Actor:
    def __init__(self, abilities):
        self.abilities = abilities

actor = Actor({"browse": "driver double"})
print(actor.abilities.get("call_api", "missing ability"))
