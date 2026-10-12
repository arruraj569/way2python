import pytest
import requests
@pytest.mark.parametrize("payload", [
    {"email": "mira@example.test"},
    {"name": "", "email": "mira@example.test"},
    {"name": "Mira", "email": "not-an-email"},
    {"name": "x" * 101, "email": "mira@example.test"},
], ids=["missing-name", "empty-name", "malformed-email", "name-too-long"])
def test_reject_invalid(payload):
    response = requests.post("http://127.0.0.1:8765/users",
        headers={"Authorization": "Bearer demo-token"}, json=payload, timeout=5)
    assert response.status_code == 422
    assert response.json()["error"] == "validation_error"
