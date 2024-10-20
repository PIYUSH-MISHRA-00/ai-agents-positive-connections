import streamlit as st
import requests

def main():
    st.title("Agent Matchmaking Platform")

    if st.button("Fetch Agents"):
        response = requests.get("http://localhost:5000/api/agents")  # Adjust the URL if necessary
        if response.status_code == 200:
            agents = response.json()
            st.write(agents)
        else:
            st.error("Error fetching agents.")

    if st.button("Show Feedback Form"):
        st.experimental_set_query_params(page="feedback")

if __name__ == "__main__":
    main()
