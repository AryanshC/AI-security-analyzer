import pandas as pd
import joblib
import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


print("Loading dataset...")

df = pd.read_csv("app/ml/data/cyber_logs.csv")


X_text = df["text"]
y = df["label"]


print("Loading embedding model...")

embedder = SentenceTransformer("all-MiniLM-L6-v2")


print("Encoding logs...")

X = embedder.encode(X_text.tolist())


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print("Training Random Forest...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


model.fit(X_train, y_train)


predictions = model.predict(X_test)


print("\nClassification Report:")
print(classification_report(y_test, predictions))


joblib.dump(
    model,
    "app/ml/security_model.pkl"
)


print("\nModel saved!")