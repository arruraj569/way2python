logs = ["timeout checkout", "timeout login", "authorization login"]
terms = [set(log.split()) for log in logs]
print(sorted(terms[0] & terms[1]))
print(terms[0] == terms[1])
