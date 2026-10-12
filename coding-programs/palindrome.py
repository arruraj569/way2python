def palindrome(text):
    normalized = "".join(character for character in text.casefold() if character.isalnum())
    return normalized == normalized[::-1]

print(palindrome("Never odd or even"))
print(palindrome("Python"))
