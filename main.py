import streamlit as st
from PIL import Image
import requests
import time

# Function to load lottie animation from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Set page configuration for the web app
st.set_page_config(page_title="Happy Birthday", page_icon="🎉", layout="centered")

# Load balloon animation from lottiefiles
lottie_balloons = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_u4yrau.json")  # Balloons animation

# Load image and audio from GitHub repository
github_base_url = "https://raw.githubusercontent.com/username/repository_name/branch_name/folder_name/"

background_image_url = github_base_url + "birthday_image.jpg"
birthday_song_url = github_base_url + "birthday_song.mp3"

# Load the image from GitHub
image = Image.open(requests.get(background_image_url, stream=True).raw)

# CSS for setting a background image and style for the page
page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("{background_image_url}"); 
    background-size: cover; 
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Sidebar navigation menu with 7 pages
st.sidebar.title("Navigation")
options = ["Home", "Page 1", "Page 2", "Page 3", "Page 4", "Page 5", "Page 6"]
choice = st.sidebar.radio("Go to", options)

# Home Page
if choice == "Home":
    st.title("🎉 Happy Birthday! 🎉")
    st.markdown("## Wishing you the happiest birthday ever filled with love, joy, and lots of surprises! 🎂🎁")
    
    # Add balloons animation
    st_lottie(lottie_balloons, height=300, key="balloons")
    
    # Add music control
    if st.button("Play Birthday Song"):
        st.audio(birthday_song_url)
    
    # Add a fun message with emojis
    st.markdown("You are amazing, and this day is all about celebrating **YOU!** 🎈🎊")
    st.markdown("Wishing you a **year** full of joy, laughter, and wonderful adventures! 🚀🌟")

# Page 1 to Page 6
else:
    st.title(f"{choice}")
    st.write("This is another page you can use to add more details for the celebration.")
    st.markdown("You can also add creative messages, photos, and fun content for each page.")
