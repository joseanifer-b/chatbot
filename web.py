# app.py

import streamlit as st
from rag_pipeline import generate_answer

st.set_page_config(page_title="MedRAG Healthcare Chatbot")

st.title("🩺 MedRAG - Healthcare AI Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask a health-related question:")

if st.button("Submit") and user_input:
    response = generate_answer(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

for role, message in st.session_state.chat_history:
    st.write(f"**{role}:** {message}")
