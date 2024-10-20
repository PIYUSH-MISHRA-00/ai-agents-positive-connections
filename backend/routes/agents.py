from flask import Blueprint, jsonify
from models.agent_model import Agent, db
from services.match_service import MatchService

agents_bp = Blueprint('agents', __name__)
match_service = MatchService(db.session)

@agents_bp.route('/api/agents', methods=['GET'])
def get_agents():
    agents = match_service.get_all_agents()
    return jsonify([agent.to_dict() for agent in agents]), 200
