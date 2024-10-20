from config import mongo
from models.user_model import User
from models.agent_model import Agent

def match_user_with_agents(user_id):
    user = mongo.db.users.find_one({"_id": user_id})
    agents = mongo.db.agents.find()

    matched_agents = [agent for agent in agents if any(expertise in user['interests'] for expertise in agent['expertise'])]
    
    return matched_agents
