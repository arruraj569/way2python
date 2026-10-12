from unittest.mock import Mock
client = Mock()
print(bool(client.get("/missing")))
client.get.return_value = None
print(bool(client.get("/missing")))
print(client.get.call_count)
