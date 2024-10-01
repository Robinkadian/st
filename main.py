import streamlit as st
from streamlit_option_menu import option_menu

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


# Sidebar menu with streamlit-option-menu
with st.sidebar:
    selected = option_menu(
        "Navigation", 
        ["Home", "Memory Page", "Puzzle Page", "Writings Page", "Music Section", "Movies & Shows", "Hidden Page"], 
        icons=['house', 'camera', 'puzzle', 'pen', 'music-note', 'film', 'lock'],
        menu_icon="cast", 
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "auto"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#ff6347"},
        }
    )



# Page content based on selection
if selected == "Home":
    st.title("🎉 Happy Birthday! 🎉")
elif selected == "Memory Page":
    st.title("📸 Memory Page")
elif selected == "Puzzle Page":
    st.title("🧩 Puzzle Page")
elif selected == "Writings Page":
    st.title("✍️ Writings Page")
elif selected == "Music Section":
    st.title("🎶 Music Section")
elif selected == "Movies & Shows":
    st.title("🎬 Movies and Shows")
elif selected == "Hidden Page":
    st.title("🕵️‍♀️ Hidden Page")
