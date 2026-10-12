import requests
with requests.Session() as client:
    client.headers.update({"Authorization": "Bearer demo-token"})
    response = client.get("http://127.0.0.1:8765/users", timeout=(2, 5))
    response.raise_for_status()
    print("Session request passed")
