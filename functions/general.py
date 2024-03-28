
import os
import streamlit as st

def save_uploaded_image(uploaded_image):
    try:
        os.makedirs("resources/images", exist_ok=True)

        image_path = os.path.join("resources", "images", uploaded_image.name)

        with open(image_path, "wb") as f:
            f.write(uploaded_image.getbuffer())
        return image_path
    except:
        return st.error("Could not save image. Please try again.")