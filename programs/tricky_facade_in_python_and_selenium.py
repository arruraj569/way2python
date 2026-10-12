def journey(login, profile):
    return login(), profile()

print(journey(lambda: "login OK", lambda: "profile rejected"))
