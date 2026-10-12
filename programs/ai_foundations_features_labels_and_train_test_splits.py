from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
data = load_iris()
train_x, test_x, train_y, test_y = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42, stratify=data.target)
print(train_x.shape, test_x.shape)
print(len(train_y), len(test_y))
