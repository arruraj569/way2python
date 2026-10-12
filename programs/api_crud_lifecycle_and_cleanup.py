import requests
from uuid import uuid4
root = "http://127.0.0.1:8765/users"
headers = {"Authorization": "Bearer demo-token"}
created = requests.post(root, headers=headers,
    json={"name": "Mira", "email": f"{uuid4().hex}@example.test"}, timeout=5)
assert created.status_code == 201
user_id = created.json()["id"]
try:
    response = requests.get(f"{root}/{user_id}", headers=headers, timeout=5)
    assert response.status_code == 200
    assert response.json()["name"] == "Mira"
    updated = requests.patch(f"{root}/{user_id}", headers=headers, json={"name": "Mira QA"}, timeout=5)
    assert updated.status_code == 200
    assert updated.json()["name"] == "Mira QA"
finally:
    deleted = requests.delete(f"{root}/{user_id}", headers=headers, timeout=5)
    assert deleted.status_code == 204
print("Lifecycle passed")
