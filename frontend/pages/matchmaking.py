import streamlit as st
import requests

def show():
    st.title("Matchmaking")

    try:
        # Attempt to fetch agents from the API
        response = requests.get("http://localhost:5000/api/agents")
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        agents = response.json()

        if agents:
            st.write("Available Agents:")
            for agent in agents:
                st.write(f"- {agent['name']} (ID: {agent['id']})")
        else:
            st.write("No agents available at the moment.")

    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while fetching agents: {str(e)}")
        st.text(f"Response content: {response.text if 'response' in locals() else 'No response'}")
    
    except requests.exceptions.JSONDecodeError:
        st.error("Failed to decode JSON response from server.")
        st.text(f"Response content: {response.text}")

    # Add more matchmaking functionality here
    st.write("Matchmaking functionality to be implemented.")

if __name__ == "__main__":
    show()