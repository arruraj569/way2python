class TextField:
    def __init__(self, store, key):
        self.store, self.key = store, key
    def fill(self, value):
        self.store[self.key] = value

class ProfileForm:
    def __init__(self, store):
        self.name = TextField(store, "name")
        self.track = TextField(store, "track")
    def update(self, name, track):
        self.name.fill(name)
        self.track.fill(track)

fields = {}
ProfileForm(fields).update("Mira", "selenium")
print(fields)
