import requests
def test_health_contract():
    response = requests.get("http://127.0.0.1:8765/health", timeout=5)
    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")
    assert response.json() == {"status": "ok"}
