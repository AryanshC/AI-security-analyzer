import streamlit as st
import requests
import plotly.express as px
import pandas as pd

if "history" not in st.session_state:
    st.session_state.history = []

# --------------------------------------------------
# Attack Information
# --------------------------------------------------

ATTACK_INFO = {
    "Normal": {
        "severity": "🟢 LOW",
        "description": "No suspicious activity detected.",
        "actions": [
            "No action required.",
            "Continue monitoring."
        ]
    },

    "BruteForce": {
        "severity": "🔴 HIGH",
        "description": "Repeated failed login attempts indicate a possible password guessing attack.",
        "actions": [
            "Block the source IP.",
            "Lock affected accounts.",
            "Review authentication logs.",
            "Notify the security team."
        ]
    },

    "Malware": {
        "severity": "☠️ CRITICAL",
        "description": "Potential malicious software activity detected.",
        "actions": [
            "Isolate affected device.",
            "Run malware scan.",
            "Review recent downloads.",
            "Escalate incident."
        ]
    },

    "SQLInjection": {
        "severity": "🟠 HIGH",
        "description": "Possible SQL Injection attack detected.",
        "actions": [
            "Validate user inputs.",
            "Review database logs.",
            "Block suspicious requests.",
            "Inspect affected endpoints."
        ]
    },

    "XSS": {
        "severity": "🟡 MEDIUM",
        "description": "Possible Cross-Site Scripting attack detected.",
        "actions": [
            "Sanitize user input.",
            "Review affected pages.",
            "Enable CSP headers.",
            "Monitor user sessions."
        ]
    }
}

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Security Analyzer",
    page_icon="🛡️",
    layout="wide"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("🛡️ AI Security Analyzer")
st.sidebar.write("Machine Learning Cybersecurity Dashboard")

st.sidebar.markdown("---")

st.sidebar.info("""
### Features

✅ FastAPI Backend

✅ Random Forest Machine Learning

✅ SentenceTransformer Embeddings

✅ Real-time Predictions

✅ Confidence Scoring
""")

# --------------------------------------------------
# Main Page
# --------------------------------------------------

st.title("🛡️ AI Security Log Analyzer")

st.caption("Analyze cybersecurity logs using Machine Learning.")

st.divider()

log = st.text_area(
    "Paste Security Log",
    height=200,
    placeholder="Example:\nFailed login attempt from unknown IP address"
)

st.divider()

st.subheader("📁 Bulk Log Analysis")

uploaded_file = st.file_uploader(
    "Upload a .txt file containing one log per line",
    type=["txt"]
)

logs = []

if uploaded_file is not None:
    logs = uploaded_file.read().decode("utf-8").splitlines()



# --------------------------------------------------
# Analyze Button
# --------------------------------------------------

if st.button("🔍 Analyze Log", use_container_width=True):

    with st.spinner("Analyzing security log..."):

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            params={"log": log}
        )

    if response.status_code != 200:
        st.error("Backend returned an error.")
        st.stop()

    result = response.json()

    prediction = result["prediction"]
    confidence = result["confidence"]

    st.session_state.history.append(
    {
        "Prediction": prediction,
        "Confidence": round(confidence * 100, 2)
    }
)

    # --------------------------------------------------
    # Risk Level
    # --------------------------------------------------

    risk = "LOW"

    if prediction in ["BruteForce", "SQLInjection"]:
        risk = "HIGH"

    elif prediction == "Malware":
        risk = "CRITICAL"

    elif prediction == "XSS":
        risk = "MEDIUM"

    info = ATTACK_INFO.get(prediction)

    st.divider()

    # --------------------------------------------------
    # Dashboard Cards
    # --------------------------------------------------

    card1, card2, card3, card4 = st.columns(4)

    with card1:
        st.metric(
            "Prediction",
            prediction
        )

    with card2:
        st.metric(
            "Severity",
            info["severity"]
        )

    with card3:
        st.metric(
            "Confidence",
            f"{confidence*100:.1f}%"
        )

    with card4:
        st.metric(
            "Risk",
            risk
        )

    st.progress(confidence)

    st.divider()

    # --------------------------------------------------
    # Description
    # --------------------------------------------------

    st.subheader("Attack Description")

    st.info(info["description"])

    # --------------------------------------------------
    # Recommended Actions
    # --------------------------------------------------

    st.subheader("Recommended Actions")

    st.success("Security Response Checklist")

    for action in info["actions"]:
        st.markdown(f"- ✅ {action}")

    st.divider()

    # --------------------------------------------------
    # Original Log
    # --------------------------------------------------

    st.subheader("Original Log")

    st.code(log, language="text")
    # --------------------------------------------------
# Bulk Log Analysis
# --------------------------------------------------

st.divider()

if st.button("📁 Analyze Uploaded File", use_container_width=True):

    if len(logs) == 0:
        st.warning("Please upload a .txt log file.")
        st.stop()

    bulk_results = []

    progress = st.progress(0)

    for i, line in enumerate(logs):

        if line.strip() == "":
            continue

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            params={"log": line}
        )

        if response.status_code == 200:

            result = response.json()

            bulk_results.append({
                "Log": line,
                "Prediction": result["prediction"],
                "Confidence": round(result["confidence"] * 100, 2)
            })

        progress.progress((i + 1) / len(logs))

    if len(bulk_results) == 0:
        st.error("No logs were analyzed.")
        st.stop()

    df = pd.DataFrame(bulk_results)

    st.success(f"Successfully analyzed {len(df)} logs.")
    total = len(df)

    normal = (df["Prediction"] == "Normal").sum()

    threats = total - normal

    high_risk = df["Prediction"].isin(
            ["Malware", "BruteForce", "SQLInjection"]
        ).sum()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Logs", total)
    c2.metric("Threats", threats)
    c3.metric("Normal", normal)
    c4.metric("High Risk", high_risk)

    st.subheader("Analysis Results")

    st.dataframe(df, use_container_width=True)

    st.subheader("Attack Distribution")

    counts = (
            df["Prediction"]
            .value_counts()
            .reset_index()
        )

    counts.columns = ["Attack", "Count"]

    fig = px.bar(
            counts,
            x="Attack",
            y="Count",
            title="Detected Attack Types"
        )

    st.plotly_chart(
            fig,
            use_container_width=True
        )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
            "⬇ Download Results CSV",
            csv,
            "security_report.csv",
            "text/csv"
        )

    # --------------------------------------------------
# Analytics Dashboard
# --------------------------------------------------

st.divider()

st.header("📊 Security Analytics")
# --------------------------------------------------
# Security Overview
# --------------------------------------------------

if len(st.session_state.history) > 0:

    history_df = pd.DataFrame(st.session_state.history)

    total_scans = len(history_df)

    threats = (
        history_df["Prediction"] != "Normal"
    ).sum()

    threat_percent = threats / total_scans

    avg_confidence = history_df["Confidence"].mean()

    top_attack = (
        history_df["Prediction"]
        .value_counts()
        .idxmax()
    )

    if threat_percent >= 0.60:
        level = "🔴 HIGH"

    elif threat_percent >= 0.30:
        level = "🟠 MEDIUM"

    else:
        level = "🟢 LOW"

    st.subheader("🛡 Security Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Threat Level", level)
    c2.metric("Threat Rate", f"{threat_percent*100:.1f}%")
    c3.metric("Avg Confidence", f"{avg_confidence:.1f}%")
    c4.metric("Top Detection", top_attack)

    st.progress(threat_percent)

if len(st.session_state.history) > 0:

    history_df = pd.DataFrame(
        st.session_state.history
    )

    col1, col2 = st.columns(2)


    with col1:

        st.subheader("Attack Distribution")

        attack_counts = (
            history_df["Prediction"]
            .value_counts()
            .reset_index()
        )

        attack_counts.columns = [
            "Attack",
            "Count"
        ]

        fig = px.pie(
            attack_counts,
            names="Attack",
            values="Count",
            title="Detected Threats"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    with col2:

        st.subheader("Confidence History")

        fig = px.line(
            history_df,
            y="Confidence",
            markers=True,
            title="Prediction Confidence"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    st.subheader("Prediction History")

    st.dataframe(
        history_df,
        use_container_width=True
    )

else:

    st.info(
        "Run predictions to generate analytics."
    )