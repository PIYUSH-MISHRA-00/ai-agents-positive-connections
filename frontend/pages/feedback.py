import streamlit as st
import requests

def show():
    st.title("Submit Feedback")

    user_id = st.text_input("Enter your User ID:")
    agent_id = st.text_input("Enter the Agent ID:")
    rating = st.slider("Rating", 1, 5)
    comments = st.text_area("Comments")

    if st.button("Submit Feedback"):
        feedback_data = {
            "user_id": user_id,
            "agent_id": agent_id,
            "rating": rating,
            "comments": comments
        }
        response = requests.post("http://localhost:5000/api/feedback", json=feedback_data)
        
        if response.status_code == 200:
            st.success("Feedback submitted successfully!")
        else:
            st.error("Failed to submit feedback.")
