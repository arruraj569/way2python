emails = ["Mira@Example.test", "mira@example.test"]
print(len(set(emails)))
normalized = [email.lower() for email in emails]
print(len(set(normalized)))
