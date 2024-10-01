import streamlit as st
import random
import time
import base64
from PIL import Image

# Set wide layout for better design
st.set_page_config(layout="wide")

# Global variables for dynamism
visit_number = random.randint(1, 100)

# Function to display balloons
def show_balloons():
    for i in range(10):
        st.balloons()
        time.sleep(0.5)

# Function to play background music
def play_music():
    st.audio("path_to_music.mp3", autoplay=True)
    st.write("Music goes here")

# First Page: Birthday Wish Page
def first_page():
    st.title("Happy Birthday, [Her Name]!")
    
    # Display balloons on first visit
    if visit_number % 2 == 0:
        show_balloons()

    # Display music button
    if st.button("Play Music"):
        play_music()
        
    # Birthday picture
    image = Image.open("media/RobinPassportSizePhoto.jpeg")
    st.image(image, caption="A special picture for a special day!", use_column_width=True)

# Memory Page: Pictures and Videos
def memory_page():
    st.title("Memory Lane")
    st.write("A collection of our memories together.")
    
    # Example to display multiple images in a grid layout
    col1, col2 = st.columns(2)
    with col1:
        st.image("media/RobinPassportSizePhoto.jpeg", caption="Memory 1", use_column_width=True)
    with col2:
        st.image("media/RobinPassportSizePhoto.jpeg", caption="Memory 2", use_column_width=True)
    
    st.video("path_to_video.mp4")

# Puzzle Page: Fun Puzzles with Rewards
def puzzle_page():
    st.title("Solve the Puzzle!")
    
    level = st.radio("Choose a level:", ('Easy', 'Medium', 'Hard'))
    
    if level == 'Easy':
        st.write("Solve this simple puzzle: [Puzzle content]")
    elif level == 'Medium':
        st.write("Here’s a medium level puzzle: [Puzzle content]")
    else:
        st.write("Time to challenge yourself: [Puzzle content]")

    if st.button("Submit Answer"):
        st.write("Great! Here’s your reward:")
        st.audio("reward_audio.mp3", autoplay=True)

# Writings Page: Interactive Writing
def writings_page():
    st.title("Our Story in Words")
    
    st.write("This page has some special writings for you!")
    
    if st.button("Reveal More"):
        st.write("Here’s more text: [special message]")
    
    if st.button("Click for a Surprise"):
        st.image("surprise_image.jpg", use_column_width=True)

# Music Section: Favorite Music
def music_page():
    st.title("Music Time!")
    st.write("Some of our favorite tracks together.")
    
    st.audio("song1.mp3", start_time=0)
    st.write("Anthem: A song that reminds us of great moments!")

# Movies and Shows Section: List of Experiences
def movies_page():
    st.title("Movies and Shows")
    st.write("Here are some of the movies and shows we watched together:")
    
    movie_list = [
        "Movie 1: Watched in theater",
        "Show 1: Watched on laptop",
        "Movie 2: Watched on phone"
    ]
    
    for movie in movie_list:
        st.write(f"- {movie}")

# Hidden Things: Puzzles and Coded Messages
def hidden_page():
    st.title("Hidden Surprises")
    
    morse_code = "... --- ..."
    st.write(f"Can you figure out this code: {morse_code}")
    
    # Add hints (no reveal option)
    st.write("Hint: It's something you use to call for help...")

# Dynamism: Pages show something different on each visit
def dynamic_effects():
    random_effect = random.choice(['Show image', 'Change color', 'Surprise text'])
    if random_effect == 'Show image':
        st.image("dynamic_image.jpg", caption="Something different every time!")
    elif random_effect == 'Change color':
        st.markdown('<style>body {background-color: lightblue;}</style>', unsafe_allow_html=True)
    elif random_effect == 'Surprise text':
        st.write("You found the surprise text!")

# Main Function to control page navigation
def main():
    st.sidebar.title("Navigate")
    options = ["First Page", "Memory Page", "Puzzle Page", "Writings Page", 
               "Music Section", "Movies and Shows Section", "Hidden Things"]
    
    choice = st.sidebar.radio("Select a page:", options)
    
    if choice == "First Page":
        first_page()
    elif choice == "Memory Page":
        memory_page()
    elif choice == "Puzzle Page":
        puzzle_page()
    elif choice == "Writings Page":
        writings_page()
    elif choice == "Music Section":
        music_page()
    elif choice == "Movies and Shows Section":
        movies_page()
    elif choice == "Hidden Things":
        hidden_page()

    dynamic_effects()

# Run the app
if __name__ == "__main__":
    main()
