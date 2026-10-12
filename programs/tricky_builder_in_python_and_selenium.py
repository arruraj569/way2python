class BadBuilder:
    def __init__(self):
        self.data = {"track": "python"}
    def build(self):
        return self.data

builder = BadBuilder()
profile = builder.build()
builder.data["track"] = "api"
print(profile["track"])
