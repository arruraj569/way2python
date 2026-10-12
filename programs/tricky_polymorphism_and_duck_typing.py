class FakeClient:
    def get(self): return "response"

def fetch(client):
    return client.get()

print(fetch(FakeClient()))
try:
    fetch({})
except TypeError:
    print("same method name, incompatible signature")
