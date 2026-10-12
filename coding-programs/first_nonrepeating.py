from collections import Counter
def first_unique(text):
    counts = Counter(text)
    return next((character for character in text if counts[character] == 1), None)

print(first_unique("swiss"))
print(first_unique("aabb"))
