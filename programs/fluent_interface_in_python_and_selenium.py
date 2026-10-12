class ProfileDraft:
    def __init__(self):
        self.values = {}
    def named(self, name):
        self.values["name"] = name
        return self
    def learning(self, track):
        self.values["track"] = track
        return self
    def save(self):
        return dict(self.values)

result = ProfileDraft().named("Mira").learning("api").save()
print(result)
