original = ["smoke"]
alias = original
independent = original.copy()
alias.append("api")
print(original)
print(independent)
print(alias is original)
