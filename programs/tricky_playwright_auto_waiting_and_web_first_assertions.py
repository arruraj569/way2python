observations = ["Loading", "Loading", "Ready"]
print(observations[0] == "Ready")
print(any(value == "Ready" for value in observations))
