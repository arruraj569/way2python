before = {"window-a"}
after = {"window-a", "window-b"}
added = after - before
print(sorted(added))
print(len(added) == 1)
