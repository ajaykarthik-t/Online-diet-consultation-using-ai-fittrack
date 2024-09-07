import streamlit as st
import base64

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# Function to encode an image file to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


# Path to the background image file
bg_image_path = "./static/bg.jpg"

# Encode the background image to base64
bg_image_base64 = get_base64_of_bin_file(bg_image_path)

st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url('data:image/jpeg;base64,{bg_image_base64}');
            background-size: cover;
        }}
    </style>
    """,
    unsafe_allow_html=True
)


st.write("# Welcome to Diet Recommendation System! 👋")

st.sidebar.success("Select a recommendation app.")

st.markdown(
    """
    A diet recommendation web application using content-based approach with Scikit-Learn, FastAPI and Streamlit.
    You can find more details and the whole project on my [repo](https://github.com/zakaria-narjis/Diet-Recommendation-System).
    """
)
