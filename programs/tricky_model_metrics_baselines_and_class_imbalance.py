truth = [0] * 9 + [1]
predicted = [0] * 10
accuracy = sum(a == b for a, b in zip(truth, predicted)) / len(truth)
positives_found = sum(a == b == 1 for a, b in zip(truth, predicted))
print(f"Accuracy: {accuracy:.0%}")
print("Positive cases found:", positives_found)
