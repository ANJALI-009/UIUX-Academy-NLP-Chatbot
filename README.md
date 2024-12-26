# UI/UX Academy Chatbot

A simple, interactive chatbot built with Streamlit and spaCy to assist users with inquiries about UI/UX Academy courses, enrollment, and support.

## Features

- Natural language processing using spaCy
- Intent-based response system
- Interactive chat interface
- Session-based chat history
- Pre-defined responses for common queries about:
  - Course information
  - Enrollment process
  - Course materials
  - Mentorship program
  - General support
  - And more

## Prerequisites

- Python 3.6+
- Streamlit
- spaCy
- spaCy's English language model (en_core_web_sm)

## Installation

1. Clone the repository
2. Install the required packages

## Usage

1. Run the Streamlit app by streamlit <run yourfilename> eg: app.py

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Start chatting with the bot by typing your questions in the input field

## Intent Categories

The chatbot can handle queries related to:
- Course inquiries
- Enrollment questions
- Course materials
- Mentorship program
- General support
- Feedback
- Basic greetings and farewells

## How It Works

1. The chatbot uses spaCy's natural language processing to analyze user input
2. It compares the input against predefined keywords for different intents
3. Uses similarity matching to find the most appropriate response
4. Maintains a chat history during the session
5. Provides relevant responses based on the detected intent



