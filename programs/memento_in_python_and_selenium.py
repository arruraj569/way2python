from copy import deepcopy

class Draft:
    def __init__(self, data):
        self.data = deepcopy(data)
    def snapshot(self):
        return deepcopy(self.data)
    def restore(self, snapshot):
        self.data = deepcopy(snapshot)

draft = Draft({"name": "Mira", "tags": ["smoke"]})
saved = draft.snapshot()
draft.data["name"] = "Edited"
draft.data["tags"].append("invalid")
draft.restore(saved)
print(draft.data)
