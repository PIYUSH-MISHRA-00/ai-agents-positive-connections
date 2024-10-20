import streamlit as st
import requests

def submit_feedback():
    st.title("Submit Feedback")
    st.markdown("Provide your valuable feedback to help us improve agent matchmaking!")

    agent_id = st.number_input("Agent ID", min_value=1, step=1)
    user_feedback = st.text_area("Your Feedback", placeholder="Enter your feedback here...")

    if st.button("Submit Feedback"):
        if user_feedback:
            response = requests.post("http://backend:5000/api/feedback", json={
                "agent_id": agent_id,
                "user_feedback": user_feedback
            })
            if response.status_code == 201:
                st.success("Feedback submitted successfully! Thank you!")
            else:
                st.error("Error submitting feedback. Please try again.")
        else:
            st.warning("Please enter your feedback before submitting.")

    st.markdown("---")
    st.subheader("Recent Feedback")
    feedback_list = get_recent_feedback(agent_id)
    if feedback_list:
        for feedback in feedback_list:
            st.markdown(f"- {feedback['user_feedback']} (Agent ID: {feedback['agent_id']})")
    else:
        st.info("No feedback available for this agent yet.")

def get_recent_feedback(agent_id):
    response = requests.get(f"http://backend:5000/api/feedback?agent_id={agent_id}")
    if response.status_code == 200:
        return response.json()
    return []

# Call the function to render the feedback submission form
if __name__ == "__main__":
    submit_feedback()
