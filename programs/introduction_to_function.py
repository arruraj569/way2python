def normalize_email(email):
    return email.strip().lower()

email = normalize_email("  Mira@Example.TEST  ")
print(email)
assert email == "mira@example.test"
