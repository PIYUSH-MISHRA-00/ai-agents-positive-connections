from flask import Blueprint, request, jsonify
from models.user_model import User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    user = User(name=data['name'], email=data['email'], interests=data['interests'])
    user.save()
    return jsonify({"message": "User created successfully"})
