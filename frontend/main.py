import streamlit as st
from pages import matchmaking, feedback

st.sidebar.title("AI Agents for Positive Connections")
page = st.sidebar.selectbox("Choose a page", ["Matchmaking", "Feedback"])

if page == "Matchmaking":
    matchmaking.show()
elif page == "Feedback":
    feedback.show()
