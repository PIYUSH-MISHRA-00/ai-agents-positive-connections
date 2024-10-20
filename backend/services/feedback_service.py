from models.user_model import User
from models.agent_model import Agent
from config import db

def match_user_with_agents(user_id):
    # Retrieve the user by ID
    user = User.query.get(user_id)
    
    if user:  # Ensure the user exists
        # Retrieve all agents from the database
        agents = Agent.query.all()

        # Find matched agents based on user's interests
        matched_agents = [
            agent for agent in agents 
            if any(expertise in user.interests for expertise in agent.expertise.split(','))
        ]
        return matched_agents
    
    return []  # Return an empty list if the user is not found
