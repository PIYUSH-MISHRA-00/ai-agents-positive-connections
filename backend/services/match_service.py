from models.user_model import User
from models.agent_model import Agent
from config import db

def match_user_with_agents(user_id):
    user = User.query.get(user_id)
    if user:
        agents = Agent.query.all()
        matched_agents = [agent for agent in agents if any(expertise in user.interests for expertise in agent.expertise.split(','))]
        return matched_agents
    return []
