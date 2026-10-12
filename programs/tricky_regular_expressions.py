import re
text = "CASE-12 trailing text"
pattern = r"CASE-\d+"
print(bool(re.match(pattern, text)))
print(bool(re.fullmatch(pattern, text)))
print(bool(re.search(pattern, "prefix CASE-12")))
