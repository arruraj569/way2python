state = {"cookies": [{"name": "demo", "value": "public-demo-value"}],
         "origins": []}
summary = {"cookie_count": len(state["cookies"])}
print(summary)
print("value" in summary)
