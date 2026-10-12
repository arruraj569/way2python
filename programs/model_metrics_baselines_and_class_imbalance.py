from sklearn.metrics import precision_score, recall_score, confusion_matrix
truth = [1, 1, 0, 0, 0]
predictions = [1, 0, 1, 0, 0]
print(precision_score(truth, predictions))
print(recall_score(truth, predictions))
print(confusion_matrix(truth, predictions).tolist())
