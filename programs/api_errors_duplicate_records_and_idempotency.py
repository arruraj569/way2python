import requests
headers = {"Authorization": "Bearer demo-token"}
url = "http://127.0.0.1:8765/users/999999"
response = requests.get(url, headers=headers, timeout=5)
assert response.status_code == 404
assert response.json()["error"] == "not_found"
print("Missing record contract passed")
