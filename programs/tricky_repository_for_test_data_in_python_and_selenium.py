from copy import deepcopy

cases = {"valid": {"roles": ["reader"]}}
shallow = cases.copy()
shallow["valid"]["roles"].append("editor")
independent = deepcopy(cases)
independent["valid"]["roles"].append("admin")
print(cases["valid"]["roles"])
