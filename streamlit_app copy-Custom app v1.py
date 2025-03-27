import streamlit as st
import base64
import time

# Function to set background image
def set_background(image_file):
    data = image_file.read()
    encoded = base64.b64encode(data).decode()
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# File uploader for background image
uploaded_bg_file = st.file_uploader("Choose a background image file", type=["jpg", "png", "jpeg"])
if uploaded_bg_file is not None:
    set_background(uploaded_bg_file)

# Add CSS for animated text
page_text_animation = '''
<style>
@keyframes textColorChange {
    0% {color: red;}
    25% {color: blue;}
    50% {color: green;}
    75% {color: purple;}
    100% {color: red;}
}

@keyframes moveText {
    0% {transform: translateY(0px);}
    25% {transform: translateY(-10px);}
    50% {transform: translateY(0px);}
    75% {transform: translateY(10px);}
    100% {transform: translateY(0px);}
}

@keyframes shrinkGrow {
    0% {transform: scale(1);}
    25% {transform: scale(1.2);}
    50% {transform: scale(1);}
    75% {transform: scale(0.8);}
    100% {transform: scale(1);}
}

@keyframes wave {
    0% {transform: rotate(0deg);}
    25% {transform: rotate(10deg);}
    50% {transform: rotate(0deg);}
    75% {transform: rotate(-10deg);}
    100% {transform: rotate(0deg);}
}

.animated-text {
    animation: textColorChange 4s infinite, moveText 2s infinite, shrinkGrow 3s infinite, wave 2s infinite;
}

.animated-text:nth-child(1) {
    animation-delay: 0s;
}

.animated-text:nth-child(2) {
    animation-delay: 0.5s;
}

.animated-text:nth-child(3) {
    animation-delay: 1s;
}

.animated-text:nth-child(4) {
    animation-delay: 1.5s;
}

.animated-text:nth-child(5) {
    animation-delay: 2s;
}
</style>
'''

st.markdown(page_text_animation, unsafe_allow_html=True)

st.markdown('<h1 class="animated-text">Hello World</h1>', unsafe_allow_html=True)

if st.button('Click me!'):
    st.markdown('<p class="animated-text">Hello from Streamlit!</p>', unsafe_allow_html=True)

name = st.text_input("Enter your name:")
if name:
    st.markdown(f'<p class="animated-text">Hello, {name}!</p>', unsafe_allow_html=True)

age = st.slider("Select your age:", 0, 100, 25)
st.markdown(f'<p class="animated-text">You are {age} years old.</p>', unsafe_allow_html=True)

option = st.selectbox(
    '<p class="animated-text">Which number do you like best?</p>',
    [1, 2, 3, 4, 5]
)
st.markdown(f'<p class="animated-text">You selected: {option}</p>', unsafe_allow_html=True)

st.markdown('<p class="animated-text">Loading...</p>', unsafe_allow_html=True)
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress_bar.progress(i + 1)
st.markdown('<p class="animated-text">Done!</p>', unsafe_allow_html=True)

# Cybersecurity facts
cyber_facts = [
    "The first computer virus was created in 1983.",
    "Over 90% of malware is delivered via email.",
    "The term 'hacker' originally referred to a skilled programmer.",
    "Ransomware attacks occur every 14 seconds.",
    "The first recorded cybercrime occurred in 1820."
]

if st.button('Generate Cybersecurity Fact'):
    fact = cyber_facts[time.time_ns() % len(cyber_facts)]
    st.markdown(f'<p class="animated-text">{fact}</p>', unsafe_allow_html=True)