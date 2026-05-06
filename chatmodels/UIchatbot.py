import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# Initialize model
model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

st.set_page_config(page_title="ChatBot UI", page_icon="🤖", layout="centered")

st.title("VibeChat 🤖✨")
st.markdown("### Choose your AI mode")

# Mode selection
mode_option = st.radio(
    "Select Mode:",
    ("Angry 😡", "Funny 😂", "Sad 😢")
)

if mode_option == "Angry 😡":
    mode = "You are an Angry agent. You response aggressively and impatiently."
elif mode_option == "Funny 😂":
    mode = "You are an Funny agent. You response humor and jokes."
elif mode_option == "Sad 😢":
    mode = "You are an Sad agent. You response in a depressed and emotional tone."

# Session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=mode)]

st.markdown("---")

# Chat display
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))
    st.chat_message("user").write(user_input)

    response = model.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))

    st.chat_message("assistant").write(response.content)