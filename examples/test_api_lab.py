"""Behavioral checks against the running local mock_api.py service."""
import os
from uuid import uuid4
import pytest
import requests

@pytest.fixture
def client():
    with requests.Session() as session:
        session.headers['Authorization'] = 'Bearer demo-token'
        yield session

@pytest.fixture
def root():
    return os.getenv('API_BASE_URL', 'http://127.0.0.1:8765').rstrip('/')

def test_health(root):
    response = requests.get(f'{root}/health', timeout=5)
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}
    assert response.headers['Content-Type'].startswith('application/json')

@pytest.mark.parametrize('authorization', [None, 'Bearer wrong-token'], ids=['missing-token','invalid-token'])
def test_unauthorized(root, authorization):
    headers = {'Authorization': authorization} if authorization else {}
    response = requests.get(f'{root}/users', headers=headers, timeout=5)
    assert response.status_code == 401
    assert response.json() == {'error': 'unauthorized'}

@pytest.mark.parametrize('payload', [
    {'email': 'mira@example.test'},
    {'name': '', 'email': 'mira@example.test'},
    {'name': 'Mira', 'email': 'invalid'},
    {'name': 'x'*101, 'email': 'mira@example.test'},
    {'name': 'Mira', 'email': 'mira@example.test', 'admin': True},
], ids=['missing-name','empty-name','invalid-email','long-name','unknown-field'])
def test_invalid_payload(client, root, payload):
    response = client.post(f'{root}/users', json=payload, timeout=5)
    assert response.status_code == 422
    assert response.json() == {'error': 'validation_error'}

def test_crud_and_duplicate(client, root):
    payload = {'name': 'Mira', 'email': f'{uuid4().hex}@example.test'}
    created = client.post(f'{root}/users', json=payload, timeout=5)
    assert created.status_code == 201
    user_id = created.json()['id']
    try:
        assert isinstance(user_id,int) and user_id > 0
        fetched = client.get(f'{root}/users/{user_id}', timeout=5)
        assert fetched.status_code == 200
        assert fetched.json() == {'id':user_id, **payload}
        duplicate = client.post(f'{root}/users', json=payload, timeout=5)
        assert duplicate.status_code == 409
        assert duplicate.json()['error'] == 'duplicate_email'
        updated = client.patch(f'{root}/users/{user_id}', json={'name':'Mira QA'}, timeout=5)
        assert updated.status_code == 200
        assert updated.json()['name'] == 'Mira QA'
        listing = client.get(f'{root}/users', params={'limit':100}, timeout=5)
        assert listing.status_code == 200
        assert any(item['id']==user_id for item in listing.json()['items'])
    finally:
        deleted = client.delete(f'{root}/users/{user_id}', timeout=5)
        assert deleted.status_code == 204
        assert deleted.content == b''
    assert client.get(f'{root}/users/{user_id}',timeout=5).status_code == 404

@pytest.mark.parametrize('length',[1,100])
def test_name_boundaries(client, root, length):
    payload = {'name':'x'*length,'email':f'{uuid4().hex}@example.test'}
    created = client.post(f'{root}/users',json=payload,timeout=5)
    assert created.status_code == 201
    user_id=created.json()['id']
    try:
        assert created.json()['name'] == payload['name']
    finally:
        assert client.delete(f'{root}/users/{user_id}',timeout=5).status_code == 204

def test_invalid_json(client, root):
    response=client.post(f'{root}/users',data='{bad',headers={'Content-Type':'application/json'},timeout=5)
    assert response.status_code == 400
    assert response.json()['error'] == 'invalid_json'
