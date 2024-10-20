from flask import Flask
from routes.users import user_bp
from routes.agents import agent_bp
from routes.feedback import feedback_bp
from config import initialize_db

app = Flask(__name__)

# Initialize MongoDB
initialize_db(app)

# Register routes
app.register_blueprint(user_bp, url_prefix='/api/users')
app.register_blueprint(agent_bp, url_prefix='/api/agents')
app.register_blueprint(feedback_bp, url_prefix='/api/feedback')

if __name__ == "__main__":
    app.run(debug=True)
