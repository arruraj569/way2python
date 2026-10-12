responses = [{"url": "/analytics", "status": 200},
             {"url": "/users", "status": 500}]
print(responses[0]["status"] == 200)
user_response = next(row for row in responses if row["url"] == "/users")
print(user_response["status"])
