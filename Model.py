from flask import Flask, request, jsonify
import tensorflow as tf
import tensorflow_hub as hub
from keras.models import load_model
from keras.layers import Layer
from keras.saving import register_keras_serializable
from keras.config import enable_unsafe_deserialization
import numpy as np

# Enable unsafe deserialization (needed for Lambda layers)
enable_unsafe_deserialization()

# Register the custom USE Layer
@register_keras_serializable()
class USELayer(Layer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

    def call(self, inputs):
        return self.use(inputs)

# Initialize Flask app
app = Flask(__name__)

# Load Keras model with custom layer
model = load_model("model.keras", custom_objects={"USELayer": USELayer})

@app.route("/", methods=["GET"])
def home():
    return "✅ Harmful Message Detector API is running."

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "texts" not in data:
        return jsonify({"error": "Missing 'texts' in request body"}), 400

    texts = data["texts"]
    try:
        input_array = np.array(texts, dtype=object)
        preds = model.predict(input_array)
        #label="Harmful" if max(preds)>0.5 else "Not Harmful"
        score=float(tf.squeeze(preds))
        return jsonify({"Score": score})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
