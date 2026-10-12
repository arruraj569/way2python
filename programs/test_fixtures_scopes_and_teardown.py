import pytest
@pytest.fixture
def users():
    records = []
    yield records
    records.clear()

def test_add_user(users):
    users.append({"name": "Mira"})
    assert len(users) == 1

def test_isolated_users(users):
    assert users == []
