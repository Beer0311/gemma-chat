import streamlit as st
import requests
import speech_recognition as sr
from streamlit_lottie import st_lottie
from datetime import datetime
import pyttsx3

# ----- Initialize pyttsx3 engine globally -----
engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')  # Default to Alex voice on macOS

# ----- Function to load Lottie animation -----
def load_lottieurl(url: str):
    try:
        res = requests.get(url)
        if res.status_code != 200:
            return None
        return res.json()
    except:
        return None

# ----- Streamlit Page Config -----
st.set_page_config(page_title="🎙️ Beer's AI Chatbot", layout="centered")

# ----- Updated Styling with Neon Border and Darker Background -----
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        margin: 0;
        padding: 0;
        color: #E5E7EB;
    }
    body {
        background: #030508; /* Darker black background */
        background-image: linear-gradient(135deg, rgba(3, 5, 8, 0.95), rgba(2, 3, 5, 0.95));
        margin: 0;
        padding: 0;
    }
    .block-container {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        min-height: 100vh;
        background: linear-gradient(135deg, rgba(3, 5, 8, 0.95), rgba(2, 3, 5, 0.95)); /* Darker container background */
        padding: 2rem 1rem;
        border-radius: 15px;
        backdrop-filter: blur(8px);
        color: #E5E7EB;
        max-width: 900px;
        margin: 2rem auto;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        border: 2px solid #00FFEA; /* Neon cyan border */
        box-shadow: 0 0 15px rgba(0, 255, 234, 0.5), 0 0 30px rgba(0, 255, 234, 0.3); /* Neon glow effect */
        overflow-y: auto;
    }
    .title-gradient {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        color: #E5E7EB; /* Light off-white for title */
        margin-bottom: 2rem;
        text-shadow: 0 0 5px rgba(229, 231, 235, 0.5); /* Subtle glow effect */
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-10px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .chat-bubble-user {
        background: #151A1E; /* Very dark gray for user bubbles */
        color: #E5E7EB;
        padding: 14px 20px;
        border-radius: 15px 15px 5px 15px;
        margin: 10px;
        max-width: 75%;
        align-self: flex-end;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    .chat-bubble-user:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 14px rgba(0, 0, 0, 0.3);
    }
    .chat-bubble-ai {
        background: #0F1317; /* Darker gray for AI bubbles */
        color: #E5E7EB;
        padding: 14px 20px;
        border-radius: 15px 15px 15px 5px;
        margin: 10px;
        max-width: 75%;
        align-self: flex-start;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    .chat-bubble-ai:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 14px rgba(0, 0, 0, 0.3);
    }
    .bottom-fixed {
        position: fixed;
        bottom: 2rem;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        max-width: 900px;
        display: flex;
        gap: 1rem;
        align-items: center;
        z-index: 1000;
        background: transparent;
        padding: 0.75rem;
    }
    .bottom-fixed button {
        padding: 0.75rem 1.25rem;
        background: #151A1E; /* Very dark gray for buttons */
        color: #E5E7EB;
        border: 1px solid #E5E7EB; /* Light border for contrast */
        border-radius: 10px;
        cursor: pointer;
        height: 45px;
        font-size: 1rem;
        font-weight: 600;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    .bottom-fixed button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 14px rgba(0, 0, 0, 0.3);
    }
    .stChatInput {
        background: #0F1317; /* Very dark input background */
        border-radius: 10px;
        padding: 0.75rem;
        border: 2px solid #E5E7EB; /* Light border */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        display: block !important;
        font-size: 1rem;
        color: #E5E7EB;
        transition: border-color 0.3s ease;
    }
    .stChatInput:focus {
        border-color: #00FFEA; /* Neon cyan border on focus */
        box-shadow: 0 0 8px rgba(0, 255, 234, 0.3);
    }
    .stButton > button {
        display: inline-block !important;
    }
    .speak-button {
        padding: 0.75rem 1.25rem;
        background: #151A1E;
        color: #E5E7EB;
        border: 1px solid #E5E7EB;
        border-radius: 10px;
        cursor: pointer;
        height: 45px;
        font-size: 1rem;
        font-weight: 600;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
        margin-left: 0.75rem;
    }
    .speak-button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 14px rgba(0, 0, 0, 0.3);
    }
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #030508; /* Match darker background */
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb {
        background: #1F2633; /* Subtle gray thumb */
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #2D3748; /* Slightly lighter on hover */
    }
    </style>
""", unsafe_allow_html=True)

# Robot animation at top
robot_animation = load_lottieurl("https://lottie.host/6f379b45-35b6-4aa3-a465-8c6b5e2cf9c8/ExMymFdBJO.json")
if robot_animation:
    st_lottie(robot_animation, speed=1, height=220, key="robot")

# Title
st.markdown("<div class='title-gradient'>🤖 Beer's AI Chatbot</div>", unsafe_allow_html=True)

# Initialize chat history and speaking state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "is_speaking" not in st.session_state:
    st.session_state.is_speaking = False
if "current_reply" not in st.session_state:
    st.session_state.current_reply = None

# Main chat container
chat_container = st.container()
with chat_container:
    for role, msg in st.session_state.chat_history:
        css_class = "chat-bubble-user" if role == "user" else "chat-bubble-ai"
        st.markdown(f'<div class="{css_class}">{msg}</div>', unsafe_allow_html=True)

# Voice recording function
def record_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:  # Fixed: Replaced inputto_speech with sr.Microphone()
        st.info("🎤 Listening... Speak now")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            return recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            return "⚠️ Listening timed out."
        except sr.UnknownValueError:
            return "⚠️ Could not understand your voice."
        except sr.RequestError:
            return "⚠️ Speech recognition error."

# Function to handle speech
def speak_text(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        st.error(f"Speech synthesis error: {e}")
    finally:
        st.session_state.is_speaking = False

# --- Bottom fixed input and mic UI ---
input_container = st.container()
with input_container:
    st.markdown('<div class="bottom-fixed">', unsafe_allow_html=True)
    cols = st.columns([8, 1, 1])
    with cols[0]:
        user_input = st.chat_input("Type a message or press 🎤", key="chatbox")
    with cols[1]:
        mic_clicked = st.button("🎤", key="mic_button")
    with cols[2]:
        speak_button = st.button("🔊", key="speak_button", help="Pause speech" if st.session_state.is_speaking else "Run speech")
    st.markdown('</div>', unsafe_allow_html=True)

if mic_clicked:
    user_input = record_voice()

# --- Process user input ---
if user_input:
    st.session_state.chat_history.append(("user", user_input))
    with chat_container:
        st.markdown(f'<div class="chat-bubble-user">{user_input}</div>', unsafe_allow_html=True)

    with st.spinner("🤖 Beer is thinking..."):
        # Handle date and time commands with additional keywords
        user_input_lower = user_input.lower().strip()
        if any(keyword in user_input_lower for keyword in ["show date", "tell me the date", "what date is it"]):
            reply = f"Current date: {datetime.now().strftime('%B %d, %Y')}"
        elif any(keyword in user_input_lower for keyword in ["show time", "tell me the time", "what time is it", "what's time", "whats time"]):
            reply = f"Current time: {datetime.now().strftime('%I:%M %p')}"
        elif "show datetime" in user_input_lower:
            reply = f"Current date and time: {datetime.now().strftime('%B %d, %Y %I:%M %p')}"
        else:
            try:
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={"model": "gemma:7b", "prompt": user_input, "stream": False}
                )
                reply = response.json()["response"]
            except Exception as e:
                reply = f"⚠️ Error: {e}"

    st.session_state.chat_history.append(("assistant", reply))
    st.session_state.current_reply = reply
    with chat_container:
        st.markdown(f'<div class="chat-bubble-ai">{reply}</div>', unsafe_allow_html=True)

# --- Handle speak button ---
if speak_button and st.session_state.current_reply:
    if st.session_state.is_speaking:
        engine.stop()  # Stop ongoing speech
        st.session_state.is_speaking = False
    else:
        st.session_state.is_speaking = True
        speak_text(st.session_state.current_reply)