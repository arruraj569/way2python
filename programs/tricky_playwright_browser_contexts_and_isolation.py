import copy
state = {"cookies": ["user-a"]}
alias = state
isolated = copy.deepcopy(state)
alias["cookies"].append("extra")
print(state["cookies"])
print(isolated["cookies"])
