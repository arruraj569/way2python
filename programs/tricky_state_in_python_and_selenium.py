state = "signed out"
observed_status = "Invalid credentials"
if observed_status == "Welcome, learner!":
    state = "signed in"
print(state)
