import streamlit as st

import subprocess
import sys

# Function to install spaCy model
def install_model():
    try:
        subprocess.check_call([sys.executable, '-m', 'spacy', 'download', 'en_core_web_sm'])
    except Exception as e:
        print(f"An error occurred while installing the model: {e}")

# Call the function to ensure the model is installed
install_model()
import spacy
import random

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Intent dictionary
intents = {
    "course_inquiry": {
        "keywords": ["course", "courses", "program", "UI/UX", "design"],
        "response": [
            "We offer the following courses:\n1. Introduction to UI/UX Design (6 weeks)\n2. Advanced UX Prototyping (8 weeks)\nLet me know if you'd like details about schedules or enrollment!"
        ]
    },
    "enrollment_question": {
        "keywords": ["enroll", "sign up", "register", "enrollment process"],
        "response": [
            "You can enroll on our website. Visit the 'Enroll Now' section to get started. Feel free to ask if you need help with the process!"
        ]
    },
    "faq_materials": {
        "keywords": ["materials", "resources", "syllabus", "study", "course content"],
        "response": [
            "All course materials are accessible through your student dashboard after enrollment. Let me know if you need help finding them!"
        ]
    },
    "faq_mentorship": {
        "keywords": ["mentorship", "mentor", "guidance", "one-on-one", "support"],
        "response": [
            "Yes, we provide weekly one-on-one mentorship sessions to assist you during the course. Feel free to ask more about the mentorship program!"
        ]
    },
    "live_chat_handover": {
        "keywords": ["help", "human", "support", "representative", "complex", "assistance"],
        "response": [
            "It seems like you need assistance with something specific. Let me connect you with a human representative for more personalized help."
        ]
    },
    "feedback": {
        "keywords": ["feedback", "review", "opinion", "suggestion"],
        "response": [
            "We value your feedback! Please share your thoughts or suggestions so we can improve our services."
        ]
    },
    "greeting": {
        "keywords": ["hello", "hi", "hey", "good morning", "good evening"],
        "response": [
            "Hello! How can I assist you today?"
        ]
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you", "talk later"],
        "response": [
            "Goodbye! Have a great day!"
        ]
    }
}

# Function to get the most similar response
def most_similar_response(user_input):
    user_doc = nlp(user_input)
    max_similarity = -1
    most_similar_response = None

    for intent, data in intents.items():
        for keyword in data["keywords"]:
            query_doc = nlp(keyword)
            similarity = user_doc.similarity(query_doc)
            
            if similarity > max_similarity:
                most_similar_response = random.choice(data["response"])
                max_similarity = similarity

        similarity_threshold = 0.7
        if max_similarity < similarity_threshold:
         most_similar_response = "I'm sorry, I don't have a response for that."
 
    return most_similar_response

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Streamlit UI
st.title("UI/UX Academy Chatbot")
st.write("Welcome! Ask me anything about our courses, enrollment, or support!")

# Input field
user_input = st.text_input("Your message")

# Button to submit
if st.button("Submit"):
    if user_input:
        # Get response from the chatbot
        response = most_similar_response(user_input)

        # Add user input and chatbot response to chat history
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Chatbot", response))

# Display chat history (moved after the input processing)
st.write("")
for role, message in st.session_state.chat_history:
    if role == "You":
        st.write(f"👤 **You:** {message}")
    else:
        st.write(f"🤖 **Chatbot:** {message}")
