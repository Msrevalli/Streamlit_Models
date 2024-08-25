import streamlit as st
from transformers import pipeline
from PIL import Image, ImageEnhance

# Initialize the chatbot pipeline
chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")

st.title("Chatbot with Image Capture and Beautification")

# Chatbot section
user_input = st.text_input("You: ", "Hello, how are you?")
if user_input:
    response = chatbot(user_input)
    st.write(f"Bot: {response['generated_text']}")

# Image capture and beautification section
img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # Read the image from the buffer
    image = Image.open(img_file_buffer)
    st.image(image, caption='Captured Image.', use_column_width=True)

    # Enhance contrast
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(1.5)
    st.image(enhanced_image, caption='Enhanced Image.', use_column_width=True)