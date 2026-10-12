import requests
response = requests.get("http://127.0.0.1:8765/users",
    headers={"Authorization": "Bearer demo-token"},
    params={"limit": 2}, timeout=5)
assert response.status_code == 200
data = response.json()
assert isinstance(data["items"], list)
assert len(data["items"]) <= 2
print("List contract passed")
