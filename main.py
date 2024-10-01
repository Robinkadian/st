import streamlit as st
import random
import qrcode
from io import BytesIO
import base64
from streamlit_player import st_player
from PIL import Image

# --- Helper functions for dynamic QR code ---
def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    return img

def display_qr(data):
    img = generate_qr(data)
    buf = BytesIO()
    img.save(buf)
    byte_im = buf.getvalue()
    st.image(byte_im, width=150)

def play_random_song():
    # A small set of YouTube video URLs
    song_list = [
        "https://www.youtube.com/watch?v=your-song-link1",  # Add song links here
        "https://www.youtube.com/watch?v=your-song-link2",
    ]
    return random.choice(song_list)

# --- First Page ---
def first_page():
    st.title("🎉 Happy Birthday to the Love of My Life! 🎉")
    st.balloons()  # Shows balloons

    # Display a lovely picture
    st.image('your_picture.jpg', caption="Here's to many more years together", use_column_width=True)

    # Optionally, add background music
    if st.button("Play Birthday Music 🎶"):
        st_player(play_random_song())

# --- Memory Page ---
def memory_page():
    st.title("📸 Our Beautiful Memories")
    images = ['memory1.jpg', 'memory2.jpg']  # Add paths to your images
    for img in images:
        st.image(img, caption="A beautiful memory together", use_column_width=True)

    videos = ['video1.mp4', 'video2.mp4']  # Add paths to your videos
    for video in videos:
        st.video(video)

# --- Puzzle Page ---
def puzzle_page():
    st.title("🧩 Fun Puzzle Challenge!")
    st.subheader("Solve this puzzle to unlock a surprise!")
    
    # Placeholder for puzzle (e.g., number puzzle or a custom game)
    if st.button("Solve Puzzle!"):
        st.success("Congratulations! Here's a surprise!")
        st_player(play_random_song())  # After solving puzzle, plays a random song/video

# --- Writings Page ---
def writings_page():
    st.title("✍️ Our Journey in Words")
    st.write("Click below to reveal more about our story:")
    
    if st.button("Reveal More"):
        st.write("I can't imagine my life without you. You're my sunshine!")
        st.image('special_moment.jpg', caption="A Special Moment")

# --- Music Section ---
def music_section():
    st.title("🎵 Our Special Playlist")
    st.write("Music that reminds me of you:")
    
    anthem_link = "https://www.youtube.com/watch?v=your-anthem-link"  # Add your music links
    st_player(anthem_link)
    
    st.write("Songs we love 🎶")
    st_player(play_random_song())

# --- Movies and Shows Section ---
def movies_and_shows():
    st.title("🎬 Movies & Shows We've Enjoyed Together")
    
    movies = ["Movie 1: Inception", "Movie 2: La La Land"]
    shows = ["Show 1: Stranger Things", "Show 2: Friends"]
    
    st.subheader("Movies:")
    for movie in movies:
        st.write(movie)

    st.subheader("Shows:")
    for show in shows:
        st.write(show)

# --- Hidden Things Page ---
def hidden_page():
    st.title("🕵️‍♀️ Hidden Secrets")
    
    secret_message = ".... .- .--. .--. -.-- / -... .. .-. - .... -.. .- -.--"  # Morse code for Happy Birthday
    st.write("Can you decipher this secret message?")
    st.write(secret_message)
    
    st.write("Hint: It's a message in Morse code 🧐")
    # Add a QR code that redirects to a hidden message
    display_qr("https://your-website-link.com")

# --- Dynamic Content Function ---
def dynamic_content():
    st.write("Each visit is a surprise!")
    styles = ["bold", "italic", "highlighted"]
    current_style = random.choice(styles)
    st.write(f"Today's surprise style is: {current_style}")

# --- Main Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["First Page", "Memory Page", "Puzzle Page", "Writings Page", "Music Section", "Movies & Shows", "Hidden Page", "Dynamic Content"])

if page == "First Page":
    first_page()
elif page == "Memory Page":
    memory_page()
elif page == "Puzzle Page":
    puzzle_page()
elif page == "Writings Page":
    writings_page()
elif page == "Music Section":
    music_section()
elif page == "Movies & Shows":
    movies_and_shows()
elif page == "Hidden Page":
    hidden_page()
elif page == "Dynamic Content":
    dynamic_content()
