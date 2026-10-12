from unittest.mock import Mock
def user_name(client, user_id):
    response = client.get(f"/users/{user_id}")
    response.raise_for_status()
    return response.json()["name"]

client = Mock()
client.get.return_value.json.return_value = {"name": "Mira"}
assert user_name(client, 7) == "Mira"
client.get.assert_called_once_with("/users/7")
print("Unit boundary passed")
