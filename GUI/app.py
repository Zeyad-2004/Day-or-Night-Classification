from PIL import Image
import streamlit as st

# Import from model.py in the same directory
from model import predict_day_night

# App Configuration
st.set_page_config(page_title="Day or Night Classifier", layout="centered")

# Header
st.markdown("""
    <h1 style='text-align: center; color: #4A90E2;'>🌅🌃 Day or Night Classifier</h1>
    <p style='text-align: center;'>Upload a photo and let the AI tell you if it's taken during the <b>day</b> or <b>night</b>.</p>
    <hr>
""", unsafe_allow_html=True)

# Upload
uploaded_file = st.file_uploader("📁 Upload an image (JPG or PNG)", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

# Main App Logic
if uploaded_file:
    image = Image.open(uploaded_file)
    
    # Prediction section
    with st.spinner("Analyzing image... ⏳"):
        label = predict_day_night(image)
    
    # Custom styling based on prediction
    if label == "Day":
        bg_color = "#FFF9E6"  # Light yellow background
        text_color = "#FFCC00"  # Gold text
        emoji = "☀️"
    else:
        bg_color = "#E6F0FF"  # Light blue background
        text_color = "#003366"  # Dark blue text
        emoji = "🌙"
    
    st.markdown(f"""
        <div style="background-color: {bg_color}; padding: 20px; border-radius: 10px; margin-bottom: 20px; text-align: center;">
            <h2 style="color: {text_color}; margin-bottom: 5px;">{emoji} Prediction: {label}</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Image display after prediction - using use_container_width instead of use_column_width
    st.image(image, caption="📸 Uploaded Image", use_container_width=True)
    
else:
    st.markdown("""
        <div style="text-align: center; padding-top: 40px;">
            <p>⬆️ Upload an image to get started.</p>
        </div>
    """, unsafe_allow_html=True)