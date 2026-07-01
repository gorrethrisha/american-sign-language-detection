import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load model
model = load_model("asl_model.keras")

# Class labels
classes = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z', 'del', 'nothing', 'space'
]

# Title
st.title("American Sign Language (ASL) Detection")
st.write("Upload an image of an ASL hand sign to predict the corresponding alphabet or gesture.")

# Upload image
uploaded_file = st.file_uploader("Choose an ASL image...",type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)

    st.image(img,caption="Uploaded Image",use_container_width=True)

    # Preprocessing
    img = img.resize((64, 64))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    prediction = model.predict(img_array)
    predicted_class = classes[np.argmax(prediction)]

    st.success(f"Predicted Sign: {predicted_class}")