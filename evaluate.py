import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the same test split (same random_state as train.py)
iris = load_iris()
X, y = iris.data, iris.target
_, X_test, _, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Load saved model
with open("artifacts/model.pkl", "rb") as f:
    model = pickle.load(f)

# Evaluate
preds = model.predict(X_test)
accuracy = accuracy_score(y_test, preds)

print(f"Accuracy: {accuracy:.4f}")

# Save result to a file so check_performance.py can read it
with open("artifacts/metrics.txt", "w") as f:
    f.write(f"{accuracy:.4f}")
