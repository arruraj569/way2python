def frequencies(text):
    counts = {}
    for word in text.casefold().split():
        counts[word] = counts.get(word, 0) + 1
    return counts

print(frequencies("api UI api"))
