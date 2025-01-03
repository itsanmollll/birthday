import streamlit as st
from PIL import Image
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Page Config
st.set_page_config(page_title="Happy Birthday!", page_icon="🎉", layout="centered")

# Welcome Page
st.title("🎉 Happy Birthday, Sonu! 🎂")
st.markdown("""
<div style="text-align: center; font-size: 20px;">
Wishing you a day filled with love, laughter, and all the things that make you happiest! 💖
</div>
""", unsafe_allow_html=True)

st.balloons()

# Memory Lane
st.header("💌")
st.markdown("Best grl in world!!:")
images = ["/Users/air/Desktop/MY PC/WORK/birthday/sonu.jpeg", "/Users/air/Desktop/MY PC/WORK/birthday/sonu1.jpeg"]
captions = ["My fav traditional!", "Cutie with attitude"]
for img, cap in zip(images, captions):
    image = Image.open(img)
    st.image(image, caption=cap)
    time.sleep(1)  # Add a delay for the emotional effect

# Add a video section
video_path = "/Users/air/Desktop/MY PC/WORK/birthday/sonu.mp4"  # Replace with your video file path
st.header("🎥 My faviourate kiss")
try:
    st.video(video_path)
except Exception as e:
    st.error(f"Error loading video: {e}")
# Personalized Quiz
st.header("🎮 Small Quiz !!")
st.markdown("Let’s see how much you know!")
score = 0

question1 = st.radio("1. Make one wish", ["To meet this year", "Watch me beast ", "E-Date "])
if question1 == "To meet this year":
    score += 1

question2 = st.radio("2.What you like most?", ["Me kissing", "Me Moaning", "Me Sleeping"])
if question2 == "Me Sleeping":
    score += 1

question3 = st.radio("3. Message for me", ["Sudhar jao", "Mai sudharungi tumko", "Tumko toh punishment hogi", "Buy you kinder joy"])
if question3 == "Tumko toh punishment hogi":
    score += 1

if st.button("Submit Answers"):
    st.write(f"Your Score: {score}/3 🎉")
    if score == 3:
        st.write("Wow! You will get a kiss 💋 ! ❤️")
    else:
        st.write("You are the best i will make these work cutie 😘")

# # Music Dedication
# st.header("🎶 A Song for You")
# st.audio("dedicated_song.mp3")  # Replace with your MP3 file path

# # Virtual Cake
# st.header("🎂 Blow Out the Candles")
# st.markdown("Click the button to blow out the candles!")
# cake_img = Image.open("cake.jpg")  # Replace with your cake image path
# if st.button("Blow Out Candles"):
#     st.image(cake_img, caption="Make a wish! 🎉")
#     st.success("Candles blown! 🕯️")

# Love Letter
st.header("💖 A Special Message")
st.markdown("""
<div style="font-size: 18px;">
Dear SOnu,

Every moment with you feels like a treasure. On this special day, I want you to know how much you mean to me. I love you so much , you are my everything.You are best and no matter how much we fight but i will try to just make you happy and kiss you and aha fuck you harder whenever we meet , you came in my life to make me feel i'm a person to be loved , i know i go sometimes and sometimes i'm kanjar but i'm your nonu naa , i love you so much , you will be having a best day everyday you are best and i know you will made it this year and you know if you don't i will love you 
            , you do whatever i just love you i love you my sweatheart!!
Thank you for being the most amazing person in my life. Happy Birthday, my love! ❤️
            
💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋
💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋
💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋💋

Love always,  
Cutu sa Nonu
</div>
""", unsafe_allow_html=True)

# Ending Surprise
st.header("🎁 Surprise!")
st.markdown("Click the button below to reveal your surprise!")
if st.button("Reveal Surprise"):
    st.markdown("Countdown to your gift reveal:")
    countdown_time = 10
    for i in range(countdown_time, 0, -1):
        st.write(f"{i} seconds remaining...")
        time.sleep(1)
    st.success("Your surprise is ready! Check your inbox for a special delivery! 🎁")
