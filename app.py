import streamlit as st
import requests

BASE_URL = "https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key=AIzaSyBE-myxHyuWxQHJfIZXLYzILLVghP6nkhA"

def send_message(message):
    url = BASE_URL
  
    payload = {
        "prompt": {
            "text": "Give me a response like a therapist for the following: " + message
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

        chat_container = st.empty()

        user_input = st.text_input("You:", "")

        if st.button("Send"):
            chat_container.text_area("You:", user_input)

            bot_response = send_message(user_input)

            chat_container.text_area("Bot:", bot_response)

    elif option == "About":
        st.markdown("### About 🌟")
        
        st.write("Welcome to Serenity Squad, your trusted mental wellness companion! \n\nWe're Team 3 - Shivani, Apoorva, Shreyash, Ronak, and Khushi - a dedicated group committed to promoting mental health awareness through innovation. Serenity Squad is our creation, a cutting-edge chatbot designed to offer guidance, encouragement, and resources for mental well-being. Our mission is simple: to break the stigma surrounding mental health and empower individuals to prioritize their mental wellness.")


if __name__ == "__main__":
    main()