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
        time.sleep(1)

# Function to play background music
def play_music():
    st.audio("media/happy-birthday-my-kitty-120918.mp3", autoplay=True)
    st.write("Happy Birthday")

# First Page: Birthday Wish Page
def HappyBirthday():
    st.title("!!!!!!!!!!!!!!!!!!!Happy Birthday, NAZNEEN!!!!!!!!!!!!!!!!!!!")

    # Display music button
    play_music()

    image = Image.open("media/Cute_with_shushee.jpeg")
    st.image(image, caption="Happy BirthDay ;-)", use_column_width=True)
    
    # Display balloons on first visit
    if visit_number % 2 == 0:
        show_balloons()

    
        
    # Birthday picture

# Memory Page: Pictures and Videos
def Memories():
    st.title("Memory Lane")
    st.write("A collection of our memories together.")
    
    # Example to display multiple images in a grid layout
    col1, col2 = st.columns(2)
    with col1:
        st.image("media/malt_daddy.jpeg", caption="Malt Daddyyyyyy", use_column_width=True)
    with col2:
        st.image("media/in_mehandi.jpeg", caption="Mehandi rachi mhare hatha mai...", use_column_width=True)
    with col2:
        st.image("media/Shushee_tu_or_rockstar.jpeg", caption="Shushee, tu, or Rockstar... wahh, wahh", use_column_width=True)
    with col2:
        st.image("media/hop_up_band.jpeg", caption="Ye to bhot mst tha, phle nhi btaya tune...", use_column_width=True)
    
    st.video("media/egg_pakoda.mp4")

# Puzzle Page: Fun Puzzles with Rewards
def Shushee_Special():
    st.title("Shushee....? Areeee wjh to yhi hai")
    
    level = st.radio("Choose a level:", ('Shushee', 'Shusheeeeee', 'Shusheeeeeeeee'))
    
    if level == 'Shushee':
        st.write("Pkka")
        st.write("")
        st.image("media/Cute_with_shushee.jpeg", caption="Memory 2", use_column_width=True)
    elif level == 'Shusheeeeee':
        st.write("Pkkaaaa")
        st.write("")
        st.image("media/Cute_with_shushee2.jpeg", caption="Memory 2", use_column_width=True)
    else:
        st.write("Pkkaaaaaaaa")
        st.write("")
        st.image("media/Cute_with_shushee3.jpeg", caption="Memory 2", use_column_width=True)


# Writings Page: Interactive Writing
def Writing():
    st.title("Although, I don't have all the writings of you...")
    
    st.write(f"""Goodbye kiss

The senses were cold , yet it was a warm day
I was enjoying my time
Though I had a longing for him to stay

“You should not go”
These were my last words as my lips stumbled through my gasped tears

There was an utter silence 
The wind started to blow 

‘’The rain is about to come, I must depart early”
That’s all he could say to cover the condolences

The bag and luggage seemed to be heavier than usual
“You don’t have to carry them”, he smiled 

In an urge to see him happy, I tried to smile 
Which failed as failed the promise of our eternal bond 

Our small and silly fights , the dances , the pranks
Suddenly a flourishing smile came to my face 
Riding our way to the airport
He could not help but ask the reason
And the ride became shorter sharing those blissful memories

As the airport approached nearer , my heart skipped a beat
My hands were cold and pale 
These last moments ,I was numb
Unaware of what to do, how to react

“ It is not in my hands , I have to shift entirely for my career”
He concluded when we were arguing about the consequences

The boarding pass went missing 
His old habit of keeping his stuff in my purse
I didn’t wanted to hand him over the pass
His tiny , shiny baby face became more weanier
I laughed as I handed him the pass 

He eyes expanded , showing the traditional anger 
I laughed and enjoyed 
Feeling his different emotions , that one last time 
Feeling his warm touch, that one last time 
His soft eyesight , wanting my sight , that one last time


I had been frozen over the waiting area
As I could not say GoodBye , that one last time

He seemed to be in a hurry 
Unhappily he dragged his handbag to the waiting area

I had a blast of mixed emotions 
As I could not see him leave 

The call for his flight arrived
I ran like I am on a sprinting fest 
I ran towards him as some force is attracting me more than ever 
The guards tried to stop ,but I could not

He seemed surprised , I shoved my arms around him 
With a speed of thousand lightbulbs
He drifted behind  and clutched me tighter

I gave him a passionate soft kiss, that one last time
“Will wait for you”  I whispered over his ears 

Riding my way back to home , I had a satisfaction 
Though that wait can become endless
What else was eternal, was that GoodBye Kiss""")
    
    if st.button("Button Dba"):
        st.write("Teri eeeeenglish is good, kbhi hindi m likh k bhi sunaaaa")
        st.video("media/tie_hair.mp4")
        
    
    if st.button("Click for a Surprise"):
        st.image("media/cute_video_call.jpeg", use_column_width=True)

# Music Section: Favorite Music
def Music():
    st.title("Music Time!")
    st.write("Savdhaan!!! Annthem k time ikdm shaant ;-)")

    if st.button("PLAY"):
        st.image("media/haiDilYeMera_poster.jpeg", use_column_width=True)
        st.audio("media/128-Hai Dil Ye Mera - Hate Story 2 128 Kbps.mp3", start_time=0)
        st.write("Ye wala sunte hi kya yaad aata hai....Bhnchod bhot kuchh")

    #st.write("Ek or hai niche potential anthem...")

# Movies and Shows Section: List of Experiences
def Movies():
    st.title("Movies to MashaAllah bhot dekhi, best out of best")
    st.write("Dekh niche likh rha hu....")

    st.image("media/rockstar_poster.jpeg", use_column_width=True)
    movie_list = [
        "Rockstar: First Theater movie watched",
        "Rick and Morty: Gaand faad...Ho gya yaar complete :-(",
        "Deadpool & Wolverine: Baby bye, bye, bye...",
        "Last Night in Soho: Fookne ka mn krr gya"
        "Laila Majanu: Hmm...very deep"
    ]
    
    for movie in movie_list:
        st.write(f"- {movie}")

# Hidden Things: Puzzles and Coded Messages
def Decode_Surprise():
    st.title("Hidden Surprises")
    
    morse_code = ".---- ..... - .... / -- .- -.-- --..-- / ..--- ----- ..--- ....- .-.-.- .-.-.- .-.-.- / .. / ... - .- .-. - . -.. / ... --- -- . - .... .. -. --. / .-. . .- .-.. .-.. -.-- / -. . .-- .-.-.- / .. / .-- .. ... .... --..-- / -.-- . / -.. .- - . / -... .... --- - / .--. .... .-.. . / -.- .. / .... --- - .. / - --- / .- .- .--- / -.- ..- -.-. .... .... / --- .-. / .... .. / -... .- .- - / .... --- - .. .-.-.- / -.- --- .. / -. .... .. --..-- / -.-. .- .-.. .-.. / -.- .-. -. .- / -- . .-. . / -.- --- --..-- / -.. . -.-. --- -.. . / -.- .-. -. . / -.- / -... .- .- -.."
    st.write(f"Can you figure out this code: {morse_code}")
    
    # Add hints (no reveal option)
    st.write("Hint: Hint to jyada jrurt nhi hai, smart enough ;-)")

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
    options = ["HappyBirthday", "Memories", "Shushee_Special", "Writing", 
               "Music", "Movies", "Decode_Surprise"]
    
    choice = st.sidebar.radio("Select a page:", options)
    
    if choice == "HappyBirthday":
        HappyBirthday()
    elif choice == "Memories":
        Memories()
    elif choice == "Shushee_Special":
        Shushee_Special()
    elif choice == "Writing":
        Writing()
    elif choice == "Music":
        Music()
    elif choice == "Movies":
        Movies()
    elif choice == "Decode_Surprise":
        Decode_Surprise()

# Run the app
if __name__ == "__main__":
    main()
