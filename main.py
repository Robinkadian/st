import streamlit as st

# --- Define Functions for Each Page ---

def home_page():
    st.title("🎉 Happy Birthday! 🎉")
    st.write("Wishing you a wonderful day filled with love and joy!")
    st.image("media/RobinPassportSizePhoto.jpeg", caption="A special birthday for someone special!", use_column_width=True)

def memory_page():
    st.title("📸 Memory Page")
    st.write("Here are all our beautiful memories together.")

def puzzle_page():
    st.title("🧩 Puzzle Page")
    st.write("Solve puzzles and win surprises!")

def writings_page():
    st.title("✍️ Writings Page")
    st.write("Here are some special writings just for you.")

def music_page():
    st.title("🎶 Music Section")
    st.write("Listen to the music that makes us feel special.")

def movies_page():
    st.title("🎬 Movies and Shows")
    st.write("Movies and shows we've enjoyed together.")

def hidden_page():
    st.title("🕵️‍♀️ Hidden Page")
    st.write("Secrets hidden within this page... Can you find them?")

# --- Sidebar Menu ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Memory Page", "Puzzle Page", "Writings Page", "Music Section", "Movies & Shows", "Hidden Page"])

# --- Page Routing ---
if page == "Home":
    home_page()
elif page == "Memory Page":
    memory_page()
elif page == "Puzzle Page":
    puzzle_page()
elif page == "Writings Page":
    writings_page()
elif page == "Music Section":
    music_page()
elif page == "Movies & Shows":
    movies_page()
elif page == "Hidden Page":
    hidden_page()
