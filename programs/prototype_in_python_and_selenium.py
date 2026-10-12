from copy import deepcopy

baseline = {"name": "Mira", "preferences": {"tracks": ["python"]}}
selenium_case = deepcopy(baseline)
selenium_case["preferences"]["tracks"].append("selenium")
print(baseline["preferences"]["tracks"])
print(selenium_case["preferences"]["tracks"])
