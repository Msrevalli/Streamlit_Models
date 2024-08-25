import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Input text box
user_input = st.text_input("Enter some text:")

# Display the input text with a greeting
if st.button("Submit"):
    st.write(f"Hello! You entered: {user_input}")

# Additional section to demonstrate more features
st.subheader("Additional Information")
st.write("This is a simple example of how to use Streamlit.")
st.write("You can use it to create interactive web apps quickly and easily.")

# Display a chart
st.subheader("Random Data Chart")
import pandas as pd
import numpy as np

# Generate random data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

# Display the chart
st.line_chart(chart_data)

# Add a slider
st.subheader("Slider Example")
slider_value = st.slider("Select a value", 0, 100)
st.write(f"You selected: {slider_value}")
