# ⚠️ Disaster Message Detector

A simple natural language powered web app that detects whether a given message is disastrous or not using a fine-tuned Universal Sentence Encoder model.

## 🔧 Tech Stack

- 🧠 TensorFlow + Keras (Flask API)
- 📦 Docker + Docker Compose
- 🎨 Streamlit UI
- 📦 Hosted on Docker Hub
- 🔍 Universal Sentence Encoder from TF Hub
- 🗣️ Nature Language Processing

---

## 🎨 UI
![image](https://github.com/user-attachments/assets/6a233ab7-463f-4d0c-9cb6-05e8a76aa882)


## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/randrothstein/harmful-message-detector.git
cd harmful-message-detector
```
### 2. Build & Run with Docker Compose
This will build both backend and frontend containers and start them up.
```bash
docker-compose up --build
```
### 3. Access the App
Backend API → http://localhost:5000

Frontend UI → http://localhost:8501


### 4. 🐳 Docker Hub (Optional)
You can pull the prebuilt backend image directly from Docker Hub:
```bash
docker pull randrothstein/harmful-detector-backend:latest
docker pull randrothstein/harmful-detector-frontend:latest
```

You can update the docker-compose.yml to as it is Docker_image_file use this image instead of building locally.
```
  backend:
    image: randrothstein/harmful-detector-backend:latest

  frontend:
    image: randrothstein/harmful-detector-ui:latest
```


## 🤖 Model
The model uses Universal Sentence Encoder (USE) from TensorFlow Hub.

Wrapped in a custom Keras layer and fine-tuned on labeled messages.
