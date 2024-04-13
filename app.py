import streamlit as st
import requests

BASE_URL = "https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key=AIzaSyBE-myxHyuWxQHJfIZXLYzILLVghP6nkhA"

def send_message(message):
    url = BASE_URL
    payload = {
        "prompt": {
            "text": "Respond to the following query like a therapist would: " + message
        }
    }
    try:
        response = requests.post(url, json=payload)
        print(response.json())
        response.raise_for_status()  
        return response.json().get("candidates", "Error: No response")[0]['output']
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def main():
    st.title("Mental Health Chatbot")
    st.sidebar.title("Options")

    option = st.sidebar.radio("Select an option:", ["Chat", "About"])

    if option == "Chat":
        st.markdown("### Chat with the Mental Health Chatbot")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Accept user input
        if prompt := st.chat_input("What is up?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                response = send_message(prompt)
                st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

    elif option == "About":
        st.markdown("### About 🌟")
        
        st.write("Welcome to Serenity Squad, your trusted mental wellness companion! \n\nWe're Team 3 - Shivani, Apoorva, Shreyash, Ronak, and Khushi - a dedicated group committed to promoting mental health awareness through innovation. Serenity Squad is our creation, a cutting-edge chatbot designed to offer guidance, encouragement, and resources for mental well-being. Our mission is simple: to break the stigma surrounding mental health and empower individuals to prioritize their mental wellness.")


if __name__ == "__main__":
    main()