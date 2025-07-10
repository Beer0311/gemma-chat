# Beer's AI Chatbot Documentation

## Overview
Beer's AI Chatbot is a web-based conversational application built using Streamlit, a Python framework for creating interactive web applications. The chatbot integrates text-based and voice-based input capabilities, powered by speech recognition and text-to-speech functionalities. It communicates with a local AI model (Gemma:7b) for generating responses and features a modern, neon-themed user interface with Lottie animations for enhanced user experience.

This documentation provides a comprehensive guide to the application’s functionality, code structure, dependencies, setup instructions, and usage details, intended for developers and users who want to understand, deploy, or extend the application.

---

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Code Structure](#code-structure)
4. [Dependencies](#dependencies)
5. [Setup Instructions](#setup-instructions)
6. [Usage](#usage)
7. [Key Components](#key-components)
   - [Streamlit Configuration](#streamlit-configuration)
   - [Lottie Animation](#lottie-animation)
   - [Speech Recognition](#speech-recognition)
   - [Text-to-Speech](#text-to-speech)
   - [Chat Interface](#chat-interface)
   - [AI Model Integration](#ai-model-integration)
8. [Styling](#styling)
9. [Session State Management](#session-state-management)
10. [Error Handling](#error-handling)
11. [Limitations](#limitations)
12. [Future Improvements](#future-improvements)
13. [Contributing](#contributing)
14. [License](#license)

---

## Features
- **Text Input**: Users can type messages in a chat input box to interact with the chatbot.
- **Voice Input**: Supports voice input using speech recognition via the `speech_recognition` library.
- **Text-to-Speech**: Responses can be vocalized using the `pyttsx3` library with a default macOS voice (Alex).
- **AI-Powered Responses**: Integrates with a local AI model (Gemma:7b) running on `localhost:11434` for generating responses.
- **Custom Commands**: Recognizes specific commands like "show date," "tell me the time," and "show datetime" for quick responses.
- **Neon-Themed UI**: A modern, dark-themed interface with neon cyan borders and animated chat bubbles.
- **Lottie Animation**: Displays a robot animation at the top for visual appeal.
- **Responsive Design**: Centered layout with a fixed bottom input bar for seamless interaction.
- **Session Persistence**: Maintains chat history using Streamlit’s session state.
- **Error Handling**: Gracefully handles speech recognition and API errors.

---

## Technologies Used
- **Python 3.8+**: Core programming language.
- **Streamlit**: Framework for building the web application.
- **requests**: For making HTTP requests to the local AI model.
- **speech_recognition**: For capturing and processing voice input.
- **pyttsx3**: For text-to-speech functionality.
- **streamlit_lottie**: For rendering Lottie animations.
- **datetime**: For handling date and time commands.
- **CSS**: Custom styles for the UI, including neon effects and animations.

---

## Code Structure
The application is contained in a single Python script (e.g., `app.py`). Below is the structure of the code:

- **Imports**: Libraries for Streamlit, HTTP requests, speech recognition, Lottie animations, date/time, and text-to-speech.
- **Global Initialization**: Sets up the `pyttsx3` engine with the Alex voice for macOS.
- **Lottie Animation Loader**: A function to fetch and parse Lottie JSON animations.
- **Streamlit Configuration**: Sets the page title and layout.
- **Custom CSS**: Defines the neon-themed styling for the UI.
- **Chat History Management**: Uses `st.session_state` to store chat history and speaking state.
- **Voice Recording Function**: Handles speech recognition using `speech_recognition`.
- **Text-to-Speech Function**: Manages speech synthesis with `pyttsx3`.
- **UI Components**: Renders the chat container, input box, and buttons (mic and speak).
- **Input Processing**: Handles user input (text or voice) and generates AI or predefined responses.
- **Button Logic**: Manages the mic and speak buttons for voice input and speech output.

---

## Dependencies
To run the application, install the following Python packages:

```bash
pip install streamlit requests speechrecognition pyttsx3 streamlit-lottie
```

Additionally, ensure the following:
- A local AI model (Gemma:7b) is running on `http://localhost:11434/api/generate`. This typically requires a model server like Ollama.
- A working microphone for voice input.
- macOS for the default Alex voice (or modify the voice property for other platforms).

---

## Setup Instructions
1. **Clone the Repository** (if hosted on GitHub):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Create a `requirements.txt` file with:
   ```
   streamlit
   requests
   speechrecognition
   pyttsx3
   streamlit-lottie
   ```

4. **Set Up the AI Model**:
   - Install Ollama (or another model server) and ensure the Gemma:7b model is available.
   - Run the model server:
     ```bash
     ollama run gemma:7b
     ```
   - Verify the server is accessible at `http://localhost:11434/api/generate`.

5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
   The app will open in your default browser at `http://localhost:8501`.

---

## Usage
1. **Access the App**: Open the application in a browser.
2. **Interact via Text**: Type a message in the input box and press Enter.
3. **Interact via Voice**: Click the 🎤 button, speak clearly, and wait for the transcription.
4. **Listen to Responses**: Click the 🔊 button to hear the latest AI response.
5. **Special Commands**:
   - "Show date" or "Tell me the date": Displays the current date.
   - "Show time" or "Tell me the time": Displays the current time.
   - "Show datetime": Displays both date and time.
6. **Pause Speech**: If speech is active, clicking the 🔊 button again will stop it.

---

## Key Components

### Streamlit Configuration
The application uses `st.set_page_config` to set the page title to "🎙️ Beer's AI Chatbot" and a centered layout for better presentation.

### Lottie Animation
The `load_lottieurl` function fetches a Lottie animation from a URL and renders it using `streamlit_lottie`. The animation is displayed at the top of the page for visual appeal.

### Speech Recognition
The `record_voice` function uses `speech_recognition` to capture audio from the microphone and transcribe it using Google’s speech-to-text API. It includes timeout and error handling for robustness.

### Text-to-Speech
The `speak_text` function uses `pyttsx3` to convert text responses to speech. It is configured with the Alex voice on macOS and includes error handling for synthesis issues.

### Chat Interface
The chat interface is built using a Streamlit container to display chat bubbles. User messages are styled with `chat-bubble-user` CSS, and AI responses use `chat-bubble-ai`. The input bar is fixed at the bottom for accessibility.

### AI Model Integration
The app sends user input to a local AI model (Gemma:7b) via a POST request to `http://localhost:11434/api/generate`. The response is parsed and displayed in the chat interface.

---

## Styling
The application features a dark, neon-themed UI with the following characteristics:
- **Background**: A dark gradient (`#030508`) for a sleek look.
- **Neon Border**: A cyan border (`#00FFEA`) with a glow effect for the main container.
- **Chat Bubbles**: User and AI messages have distinct styles with hover animations.
- **Input Bar**: Fixed at the bottom with a dark input field and neon focus effects.
- **Custom Scrollbar**: Matches the dark theme with a subtle gray thumb.
- **Animations**: The title uses a fade-in animation, and buttons scale on hover.

The CSS is injected using `st.markdown` with `unsafe_allow_html=True`.

---

## Session State Management
Streamlit’s `st.session_state` is used to persist:
- `chat_history`: A list of tuples `(role, message)` for user and AI messages.
- `is_speaking`: A boolean to track if speech synthesis is active.
- `current_reply`: Stores the latest AI response for text-to-speech.

---

## Error Handling
- **Speech Recognition**:
  - Handles `WaitTimeoutError` for no input within 5 seconds.
  - Handles `UnknownValueError` for unintelligible speech.
  - Handles `RequestError` for API issues.
- **Text-to-Speech**: Catches and displays synthesis errors.
- **AI Model**: Handles HTTP request failures and displays errors in the chat.

---

## Limitations
- **Platform Dependency**: The Alex voice is macOS-specific; other platforms require voice configuration.
- **Local AI Model**: Requires a running model server (e.g., Ollama) on `localhost:11434`.
- **Internet Dependency**: Speech recognition relies on Google’s API, requiring an internet connection.
- **Single Language**: Currently supports English for speech recognition and synthesis.
- **No Persistent Storage**: Chat history is session-based and resets on app restart.

---

## Future Improvements
- **Cross-Platform Voice Support**: Add voice configuration for Windows and Linux.
- **Persistent Chat History**: Store chat history in a database or file.
- **Multilingual Support**: Extend speech recognition and synthesis to other languages.
- **Custom AI Models**: Allow users to select different AI models or APIs.
- **Enhanced Animations**: Add more interactive Lottie animations for responses.
- **Accessibility**: Improve keyboard navigation and screen reader support.

---



## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
