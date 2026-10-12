allowed = {"timeout", "authorization", "validation"}
expected, proposed = "authorization", "timeout"
print("Valid shape:", proposed in allowed)
print("Correct label:", proposed == expected)
