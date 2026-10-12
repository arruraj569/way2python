def case(name, *, expected=200, tags=None):
    return {"name": name, "expected": expected,
            "tags": list(tags) if tags is not None else []}

print(case("login", expected=201, tags=["smoke"]))
