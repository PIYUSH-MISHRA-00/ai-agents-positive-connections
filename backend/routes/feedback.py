from flask import Blueprint, request, jsonify
from models.feedback_model import Feedback

feedback_bp = Blueprint('feedback_bp', __name__)

@feedback_bp.route('/', methods=['POST'])
def submit_feedback():
    data = request.json
    feedback = Feedback(user_id=data['user_id'], agent_id=data['agent_id'], rating=data['rating'], comments=data['comments'])
    feedback.save()
    return jsonify({"message": "Feedback submitted successfully"})
