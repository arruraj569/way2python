def choose_pattern(problem):
    choices = {
        "changing locators": "Page Object Model",
        "different algorithms": "Strategy",
        "different browsers": "Factory Method",
        "cleanup on failure": "Context managers",
    }
    return choices.get(problem, "Start with a function")

for problem in ["changing locators", "cleanup on failure", "one click"]:
    print(problem, "->", choose_pattern(problem))
print("Choose for a real problem, then keep the interface small.")
