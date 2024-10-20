import streamlit as st
from pages import feedback, matchmaking

# Set the page configuration
st.set_page_config(
    page_title="AI Agent Matchmaking",
    page_icon="🤖",
    layout="wide",
)

def main():
    st.title("AI-Driven Agent Matchmaking Platform")
    st.markdown(
        """
        Welcome to the **AI Agent Matchmaking Platform**! 🎉  
        This platform connects you with agents based on your preferences and feedback.  
        Choose an option from the sidebar to get started.
        """
    )

    # Sidebar navigation
    st.sidebar.title("Navigation")
    options = ["Matchmaking", "Submit Feedback"]
    choice = st.sidebar.radio("Select an option:", options)

    if choice == "Matchmaking":
        matchmaking.matchmaking()
    elif choice == "Submit Feedback":
        feedback.submit_feedback()

if __name__ == "__main__":
    main()
