import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Set the GOOGLE_API_KEY from Streamlit secrets
os.environ['GOOGLE_API_KEY'] = st.secrets["GOOGLE_API_KEY"]

# Initialize model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]

st.title("🧠 Gemini Chat Assistant")

# Chat interface
user_input = st.chat_input("Say something...")

# Handle user input
if user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    # Get LLM response
    with st.spinner("Thinking..."):
        result = llm.invoke(st.session_state.chat_history)

    # Append AI response to history
    st.session_state.chat_history.append(AIMessage(content=result.content))

# Display chat history
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)
