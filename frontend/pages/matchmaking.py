import streamlit as st
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:5000")

def matchmaking():
    st.title("Matchmaking Page")
    st.markdown("Click the button below to find agents that match your needs!")

    if st.button("Fetch Agents for Matchmaking"):
        response = requests.get(f"{BACKEND_URL}/api/agents")  
        if response.status_code == 200:
            agents = response.json()
            if agents:
                st.subheader("Available Agents")
                for agent in agents:
                    st.markdown(f"### {agent['name']}")
                    st.write(f"**Specialty:** {agent['specialty']}")
                    st.write("---")
            else:
                st.info("No agents available at the moment.")
        else:
            st.error("Error fetching agents.")

    st.markdown(
        """
        ### How It Works:
        1. Click the **Fetch Agents for Matchmaking** button.
        2. Review the list of available agents.
        3. Choose an agent and provide your feedback to help improve our services!
        """
    )

if __name__ == "__main__":
    matchmaking()
