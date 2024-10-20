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
        
        try:
            response = requests.post("http://localhost:5000/api/feedback", json=feedback_data, timeout=5)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            
            if response.status_code == 200:
                st.success("Feedback submitted successfully!")
            else:
                st.error(f"Unexpected status code: {response.status_code}")
                st.text(f"Response content: {response.text}")
        
        except requests.exceptions.RequestException as e:
            st.warning("Unable to connect to the backend server. Using mock submission instead.")
            st.info("In a production environment, this would be submitted to a backend server.")
            st.success("Feedback submitted successfully! (Mock)")
            st.json(feedback_data)
        
        except requests.exceptions.JSONDecodeError:
            st.error("Failed to decode JSON response from server.")
            st.text(f"Response content: {response.text}")

if __name__ == "__main__":
    show()