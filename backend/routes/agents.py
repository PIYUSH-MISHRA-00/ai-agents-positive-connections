from flask import Blueprint, request, jsonify
from services.match_service import match_user_with_agents

agent_bp = Blueprint('agent_bp', __name__)

@agent_bp.route('/match/<user_id>', methods=['GET'])
def match_user(user_id):
    agents = match_user_with_agents(user_id)
    return jsonify(agents)
