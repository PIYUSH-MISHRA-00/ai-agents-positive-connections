from flask import Blueprint, request, jsonify
from models.feedback_model import Feedback
from app import db

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/api/feedback', methods=['POST'])
def submit_feedback():
    data = request.json
    new_feedback = Feedback(agent_id=data['agent_id'], user_feedback=data['user_feedback'])
    db.session.add(new_feedback)
    db.session.commit()
    return jsonify(new_feedback.to_dict()), 201

@feedback_bp.route('/api/feedback', methods=['GET'])
def get_feedback():
    agent_id = request.args.get('agent_id')
    feedback_list = Feedback.query.filter_by(agent_id=agent_id).all()
    return jsonify([feedback.to_dict() for feedback in feedback_list]), 200
