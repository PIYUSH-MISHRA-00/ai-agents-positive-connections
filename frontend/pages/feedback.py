import streamlit as st
import requests

def submit_feedback():
    st.title("Submit Feedback")

    agent_id = st.number_input("Agent ID", min_value=1)
    user_feedback = st.text_area("Your Feedback")

    if st.button("Submit Feedback"):
        response = requests.post("http://localhost:5000/api/feedback", json={
            "agent_id": agent_id,
            "user_feedback": user_feedback
        })
        if response.status_code == 201:
            st.success("Feedback submitted successfully!")
        else:
            st.error("Error submitting feedback.")

if __name__ == "__main__":
    submit_feedback()
