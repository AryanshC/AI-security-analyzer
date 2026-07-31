# 🛡️ AI Security Log Analyzer

An end-to-end machine learning cybersecurity application that analyzes security logs and classifies potential threats using semantic text embeddings and a Random Forest classifier.

The application combines a **SentenceTransformer-based ML pipeline**, **FastAPI REST API**, and **Streamlit dashboard** to provide real-time security log analysis, confidence scoring, bulk log analysis, and security response recommendations.

## 🚀 Features

* 🤖 Machine learning-based security log classification
* 🧠 SentenceTransformer semantic embeddings
* 🌲 Random Forest classification model
* ⚡ FastAPI REST API for real-time inference
* 📊 Interactive Streamlit cybersecurity dashboard
* 📁 Bulk analysis of `.txt` log files
* 📈 Attack distribution and confidence analytics
* 🎯 Model confidence scoring
* 🛡️ Risk and severity classification
* ✅ Recommended security response actions
* ⬇️ CSV export for bulk analysis results
* 💾 Serialized ML model using Joblib

## 🧠 Machine Learning Pipeline

The application processes security logs through the following pipeline:

```text
Security Log
     ↓
SentenceTransformer
     ↓
Semantic Embedding
     ↓
Random Forest Classifier
     ↓
Predicted Attack Type
     ↓
Confidence Score
     ↓
Streamlit Dashboard
```

The model uses `all-MiniLM-L6-v2` to convert log text into numerical semantic embeddings before classification.

## 🔍 Supported Classifications

The current model supports five security event categories:

| Classification | Description                                           |
| -------------- | ----------------------------------------------------- |
| Normal         | No suspicious activity detected                       |
| BruteForce     | Possible password guessing or repeated login attempts |
| Malware        | Potential malicious software activity                 |
| SQLInjection   | Possible SQL injection activity                       |
| XSS            | Possible Cross-Site Scripting activity                |

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │   Streamlit UI      │
                    │  Security Dashboard │
                    └──────────┬──────────┘
                               │
                               │ HTTP POST
                               ▼
                    ┌─────────────────────┐
                    │    FastAPI API      │
                    │     /predict        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ SentenceTransformer │
                    │ Semantic Embeddings │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Random Forest ML   │
                    │     Classifier       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Prediction +        │
                    │ Confidence Score    │
                    └─────────────────────┘
```

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### Machine Learning

* Scikit-learn
* SentenceTransformers
* NumPy
* Pandas
* Joblib

### Frontend

* Streamlit
* Plotly

### Development Tools

* Git
* GitHub

## 📂 Project Structure

```text
ai-security-analyzer/
│
├── app/
│   ├── main.py
│   ├── anomaly.py
│   ├── embeddings.py
│   ├── ingest.py
│   ├── mcp_tools.py
│   ├── rag.py
│   │
│   └── ml/
│       ├── data/
│       │   └── cyber_logs.csv
│       ├── generate_dataset.py
│       ├── predict.py
│       ├── train_model.py
│       ├── security_model.pkl
│       └── label_encoder.pkl
│
├── ui/
│   └── app.py
│
├── .gitignore
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/AryanshC/AI-security-analyzer.git
cd AI-security-analyzer
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Running the Application

### 1. Start the FastAPI backend

From the project root:

```bash
python -m uvicorn app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

FastAPI's interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

### 2. Start the Streamlit dashboard

Open another terminal, activate the virtual environment, and run:

```bash
streamlit run ui/app.py
```

The dashboard will be available at:

```text
http://localhost:8501
```

## 🧪 Example

Example security log:

```text
Failed login attempt from unknown IP address
```

The application sends the log to the FastAPI backend, generates a semantic embedding, and passes the embedding to the trained classifier.

The dashboard then displays:

* Predicted attack category
* Severity
* Risk level
* Model confidence
* Attack description
* Recommended security response actions

## 📊 Dashboard

The Streamlit dashboard provides:

* Individual log analysis
* Bulk `.txt` log analysis
* Prediction results
* Confidence scoring
* Threat severity
* Attack distribution charts
* Prediction history
* Confidence history
* CSV report export

## 📈 Bulk Log Analysis

Users can upload a `.txt` file containing one security log per line.

The application analyzes each entry and produces a table containing:

```text
Log | Prediction | Confidence
```

The results can then be exported as a CSV security report.

## 🔐 Security Response Recommendations

For detected threats, the dashboard provides recommended response actions.

Examples include:

* Blocking suspicious IP addresses
* Reviewing authentication logs
* Isolating affected devices
* Reviewing database logs
* Sanitizing user input
* Monitoring affected sessions

## 🎯 Project Goals

This project was built to demonstrate practical experience with:

* Machine learning classification
* Natural language processing
* Semantic embeddings
* REST API development
* Full-stack application development
* Data processing
* Model deployment and inference
* Interactive data visualization
* Cybersecurity-focused application design

## ⚠️ Disclaimer

This project is intended for educational and portfolio purposes. Predictions should not be treated as definitive security findings or as a replacement for professional security monitoring and incident-response systems.
