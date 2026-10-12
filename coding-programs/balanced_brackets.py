def balanced(text):
    expected = {")": "(", "]": "[", "}": "{"}
    stack = []
    for character in text:
        if character in expected.values():
            stack.append(character)
        elif character in expected:
            if not stack or stack.pop() != expected[character]:
                return False
    return not stack

print(balanced("{[()]}"))
print(balanced("([)]"))
print(balanced("(("))
