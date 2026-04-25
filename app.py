import streamlit as st
from PIL import Image
from ai_engine import analyze_crop

st.set_page_config(page_title="CropDoctor AI", layout="centered")

# HEADER
st.markdown("""
    <h1 style='text-align: center; color: green;'>🌾 CropDoctor AI</h1>
    <p style='text-align: center;'>Gemma 4 Powered Crop Disease Assistant</p>
""", unsafe_allow_html=True)

st.divider()

# INPUT SECTION
option = st.radio("Choose input type:", ["Upload Image", "Describe Symptoms"])

input_data = None

if option == "Upload Image":
    file = st.file_uploader("Upload crop leaf image", type=["jpg", "png", "jpeg"])
    if file:
        image = Image.open(file)
        st.image(image, caption="Uploaded Leaf", use_column_width=True)
        input_data = "image_uploaded"

else:
    input_data = st.text_area("Describe crop symptoms")

# BUTTON
if st.button("🔍 Analyze Crop"):
    if input_data:
        with st.spinner("Analyzing crop health..."):
            result = analyze_crop(input_data)

        st.success("Analysis Complete")

        st.subheader("🤖 AI Result")

        st.write("### 🌿 Disease:")
        st.info(result["disease"])

        st.write("### ⚠️ Severity:")
        st.warning(result["severity"])

        st.write("### 🌱 Recommendations:")
        for i in result["advice"]:
            st.write("✔", i)

    else:
        st.error("Please provide input first")