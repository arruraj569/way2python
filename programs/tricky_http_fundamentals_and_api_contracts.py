statuses = [200, 201, 204, 302, 404]
print([status for status in statuses if 200 <= status < 300])
expected_create = 201
print(200 == expected_create)
