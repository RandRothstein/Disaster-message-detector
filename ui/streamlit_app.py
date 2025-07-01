import streamlit as st
import requests

st.set_page_config(page_title="Disaster Message Detector", page_icon="⚠️", layout="centered")

st.title("⚠️ Disaster Message Detector")
st.markdown("Enter a message and check if it's harmful.")

user_input = st.text_area("📝 Your Message", height=200, placeholder="Type your message here...")

if st.button("Analyze"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a message.")
    else:
        with st.spinner("Analyzing..."):
            try:
                response = requests.post(
                    "http://ml_backend:5000/predict",
                    json={"texts": [user_input]},
                    timeout=10
                )
                if response.status_code == 200:
                    prediction = response.json()["Score"]
                    result = "🚫 Disaster Detected" if prediction > 0.5 else "✅ Safe"
                    st.success(f"Prediction: **{result}** ({prediction:.2f})")
                else:
                    st.error("❌ Backend error. Please try again.")
            except requests.exceptions.RequestException as e:
                st.error(f"🚫 Could not connect to backend: {e}")
