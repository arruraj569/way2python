from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
data = load_iris()
train_x, test_x, train_y, test_y = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42, stratify=data.target)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=300))
model.fit(train_x, train_y)
predictions = model.predict(test_x)
assert predictions.shape == test_y.shape
print("Held-out predictions:", len(predictions))
