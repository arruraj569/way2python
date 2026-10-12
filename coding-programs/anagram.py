from collections import Counter
def letters(text):
    return Counter(character for character in text.casefold() if character.isalpha())
def anagrams(first, second):
    return letters(first) == letters(second)

print(anagrams("Listen", "Silent"))
print(anagrams("hello", "world"))
