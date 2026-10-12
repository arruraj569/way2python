import re
pattern = re.compile(r"CASE-(\d+)")
text = "Failures: CASE-12 and CASE-48"
print(pattern.findall(text))
print(bool(pattern.fullmatch("CASE-12")))
