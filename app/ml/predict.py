import joblib
import numpy as np
from sentence_transformers import SentenceTransformer

model = joblib.load("app/ml/security_model.pkl")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def predict_log(log_text: str):

    embedding = embedder.encode([log_text])
    embedding = np.array(embedding)

    prediction = model.predict(embedding)[0]

    probabilities = model.predict_proba(embedding)[0]
    confidence = float(max(probabilities))

    return {
        "log": log_text,
        "prediction": prediction,
        "confidence": confidence
    }