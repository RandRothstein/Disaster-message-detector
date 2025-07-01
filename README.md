# ⚠️ Disaster Message Detector

A simple natural language powered web app that detects whether a given message is disastrous or not using a fine-tuned Universal Sentence Encoder model.

## 🔧 Tech Stack

- 🧠 TensorFlow + Keras (Flask API)
- 📦 Docker + Docker Compose
- 🎨 Streamlit UI
- 📦 Hosted on Docker Hub
- 🔍 Universal Sentence Encoder from TF Hub
- Nature Language Processing

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/randrothstein/harmful-message-detector.git
cd harmful-message-detector
```
Build & Run with Docker Compose
```docker-compose up --build```
Backend (Flask): http://localhost:5000

Frontend (Streamlit): http://localhost:8501

🐳 Docker Hub Images
You can also pull the pre-built containers:

'''docker pull randrothstein/harmful-detector-backend:latest'''
