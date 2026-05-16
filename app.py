import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Ananya Chatbot",
    page_icon="🤖"
)

# Configure Gemini API
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("Ananya AI ChatBot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
prompt = st.chat_input("Type your message")

if prompt:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Show user message
    with st.chat_message("user"):
        st.write(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = model.generate_content(prompt)

            ai_response = response.text

            st.write(ai_response)

            # Store AI response
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": ai_response
                }
            )
