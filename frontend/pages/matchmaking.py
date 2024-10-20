import streamlit as st
import requests

def show():
    st.title("Matchmaking with AI Agents")

    user_id = st.text_input("Enter your User ID:")
    if st.button("Find Matching Agents"):
        response = requests.get(f"http://localhost:5000/api/agents/match/{user_id}")
        agents = response.json()
        
        if agents:
            st.subheader("Matched Agents:")
            for agent in agents:
                st.write(f"**Name**: {agent['name']}, **Expertise**: {', '.join(agent['expertise'])}")
        else:
            st.write("No matching agents found.")
