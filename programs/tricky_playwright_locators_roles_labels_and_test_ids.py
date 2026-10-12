buttons = [{"name": "Save", "form": "profile"},
           {"name": "Save", "form": "settings"}]
matches = [button for button in buttons if button["name"] == "Save"]
scoped = [button for button in matches if button["form"] == "profile"]
print(len(matches), len(scoped))
print(scoped[0]["form"])
