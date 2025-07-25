# Dockerfile (for backend)
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y curl
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "Model.py"]