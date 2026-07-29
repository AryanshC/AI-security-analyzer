import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(df):

    features = pd.DataFrame()

    features["failed_login"] = (df["status"] == "failed").astype(int)
    features["login_event"] = (df["event"] == "login").astype(int)

    model = IsolationForest(contamination=0.2, random_state=42)

    df["anomaly"] = model.fit_predict(features)

    return df