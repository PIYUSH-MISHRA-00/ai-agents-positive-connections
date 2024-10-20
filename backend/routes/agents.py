from flask import Blueprint, jsonify
from models.agent_model import Agent

agents_bp = Blueprint('agents', __name__)

@agents_bp.route('/api/agents', methods=['GET'])
def get_agents():
    agents = Agent.query.all()
    return jsonify([agent.to_dict() for agent in agents]), 200
