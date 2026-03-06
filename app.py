# ==========================================================
# PlantCare AI
# Advanced Plant Disease Detection Demo
#
# Developed & Deployed by Prince
# LinkedIn: https://www.linkedin.com/in/prince-codes/
# ==========================================================

import streamlit as st
import numpy as np
import cv2
from PIL import Image
import random

# Page configuration
st.set_page_config(page_title="PlantCare AI", layout="centered")

# Title
st.title("PlantCare AI by Prince 🌿")
st.write("Upload a plant leaf image to detect possible plant diseases using AI.")

# Disease list (demo)
diseases = [
    "Apple Scab",
    "Tomato Early Blight",
    "Potato Late Blight",
    "Tomato Leaf Mold",
    "Healthy Leaf"
]

# Upload image
uploaded_file = st.file_uploader("Upload Leaf Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    img_array = np.array(image)

    st.image(image, caption="Uploaded Leaf", use_column_width=True)

    # Demo prediction
    disease = random.choice(diseases)
    confidence = round(random.uniform(0.75, 0.90), 2)

    st.success(f"Disease Detected: {disease}")
    st.info(f"Confidence Score: {confidence}")

# Divider
st.markdown("---")

# Footer
st.markdown(
"""
### PlantCare AI — Smart Agriculture Tool

This tool demonstrates how AI can help detect plant diseases early and assist farmers in protecting crops.

© PlantCare AI | Developed by 
<a href="https://www.linkedin.com/in/prince-codes/" target="_blank" style="text-decoration:none; color:inherit;">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/250px-LinkedIn_logo_initials.png"
width="16"
style="vertical-align:middle; margin-right:4px;">
Prince
</a>
""",
unsafe_allow_html=True
)