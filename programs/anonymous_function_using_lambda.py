results = [{"name": "login", "seconds": 1.4},
           {"name": "search", "seconds": 0.8}]
ordered = sorted(results, key=lambda item: item["seconds"])
print([item["name"] for item in ordered])
print((lambda value: value * 1000)(0.25))
