import requests
import pytest
from uuid import uuid4

def build_user():
    return {"name": "Mira", "email": f"{uuid4().hex}@example.test"}

class UsersClient:
    def __init__(self, session):
        self.session = session
        self.root = "http://127.0.0.1:8765/users"
    def create(self, data):
        return self.session.post(self.root, json=data, timeout=5)
    def remove(self, identity):
        return self.session.delete(f"{self.root}/{identity}", timeout=5)

@pytest.fixture
def users_client():
    with requests.Session() as session:
        session.headers["Authorization"] = "Bearer demo-token"
        yield UsersClient(session)

def test_create_user(users_client):
    data = build_user()
    response = users_client.create(data)
    assert response.status_code == 201
    identity = response.json()["id"]
    try:
        assert response.json()["name"] == data["name"]
    finally:
        assert users_client.remove(identity).status_code == 204
