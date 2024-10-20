from flask import Blueprint, request, jsonify
from models.feedback_model import Feedback, db
from services.feedback_service import FeedbackService

feedback_bp = Blueprint('feedback', __name__)
feedback_service = FeedbackService(db.session)

@feedback_bp.route('/api/feedback', methods=['POST'])
def submit_feedback():
    data = request.json
    feedback = feedback_service.submit_feedback(data['agent_id'], data['user_feedback'])
    return jsonify(feedback.to_dict()), 201
