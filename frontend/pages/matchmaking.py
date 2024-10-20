import streamlit as st
import requests

def matchmaking():
    st.title("Matchmaking Page")

    if st.button("Fetch Agents for Matchmaking"):
        response = requests.get("http://localhost:5000/api/agents")
        if response.status_code == 200:
            agents = response.json()
            st.write(agents)
        else:
            st.error("Error fetching agents.")

if __name__ == "__main__":
    matchmaking()
