import streamlit as st
import random
import time

st.write("Streamlit loves LLMs!, [We can build our own chatbot app](<hyperlink>) in minutes.. then make it powerful by adding different widgets...")

st.caption("Note that this is only demo app not actually connected with LLMs")

# initally we need to initalie chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role" : "assistant", "content": "Let's start chatting!.."}]

# Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# accept user input
if prompt := st.chat_input("What is up?"):
    # then we need to add this into our chat history
    st.session_state.messages.append({"role" : "user", "content" : prompt})

    # now display this on chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # for the current prompt we need to add assistant response as well right..
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = random.choice(
            [
                "Hello there! How can I assist you today?",
                "Do you need help?",
                "Remember to drink plenty of water throughout the day to stay hydrated.",
                "Schedule your annual check-up to keep track of your overall health.",
                "Regular exercise helps improve both physical and mental health."
            ]
        )

        # now simulate stream of response with miliiseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(2)
            # add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role" : "assistant", "content" : full_response})