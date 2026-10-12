from unittest.mock import Mock
response = Mock()
response.status_code = 200
response.json.return_value = {"name": "Wrong user"}
print(response.status_code == 200)
print(response.json()["name"] == "Mira")
