import streamlit as st

# --- Define Functions for Each Page ---

st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f0f5;
    }
    .sidebar .sidebar-content h2 {
        color: #ff6347;
        font-size: 24px;
    }
    .menu-item {
        background-color: #ff6347;
        color: white;
        padding: 10px;
        margin: 5px;
        border-radius: 5px;
        text-align: center;
        font-size: 18px;
        cursor: pointer;
    }
    .menu-item:hover {
        background-color: #ff4500;
    }
    </style>
    <div class="menu-item" onclick="window.location.href='#home';">Home</div>
    <div class="menu-item" onclick="window.location.href='#memory';">Memory Page</div>
    <div class="menu-item" onclick="window.location.href='#puzzle';">Puzzle Page</div>
    <div class="menu-item" onclick="window.location.href='#writings';">Writings Page</div>
    <div class="menu-item" onclick="window.location.href='#music';">Music Section</div>
    <div class="menu-item" onclick="window.location.href='#movies';">Movies & Shows</div>
    <div class="menu-item" onclick="window.location.href='#hidden';">Hidden Page</div>
    """, unsafe_allow_html=True)

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
if st.experimental_get_query_params().get("page", ["home"])[0] == "home":
    st.title("🎉 Happy Birthday! 🎉")
    st.write("Wishing you a wonderful day filled with love and joy!")
elif st.experimental_get_query_params().get("page", ["home"])[0] == "memory":
    st.title("📸 Memory Page")
elif st.experimental_get_query_params().get("page", ["home"])[0] == "puzzle":
    st.title("🧩 Puzzle Page")
elif st.experimental_get_query_params().get("page", ["home"])[0] == "writings":
    st.title("✍️ Writings Page")
elif st.experimental_get_query_params().get("page", ["home"])[0] == "music":
    st.title("🎶 Music Section")
elif st.experimental_get_query_params().get("page", ["home"])[0] == "movies":
    st.title("🎬 Movies and Shows")
elif st.experimental_get_query_params().get("page", ["home"])[0] == "hidden":
    st.title("🕵️‍♀️ Hidden Page")
