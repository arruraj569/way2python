from sklearn.feature_extraction.text import TfidfVectorizer
logs = ["login timeout waiting for button", "search timeout waiting for results",
        "invalid token authorization failed"]
vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(logs)
print(matrix.shape[0])
print("timeout" in vectorizer.get_feature_names_out())
