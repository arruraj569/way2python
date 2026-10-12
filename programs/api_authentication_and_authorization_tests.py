import requests
url = "http://127.0.0.1:8765/users"
for headers in [{}, {"Authorization": "Bearer wrong-token"}]:
    response = requests.get(url, headers=headers, timeout=5)
    assert response.status_code == 401
    assert response.json()["error"] == "unauthorized"
print("Unauthorized cases passed")
