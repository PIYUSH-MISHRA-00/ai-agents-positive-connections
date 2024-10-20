from flask import Flask
from config import Config
from models.agent_model import db
from routes.agents import agents_bp
from routes.feedback import feedback_bp
from routes.users import users_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Register Blueprints
app.register_blueprint(agents_bp)
app.register_blueprint(feedback_bp)
app.register_blueprint(users_bp)

with app.app_context():
    db.create_all()  # Create database tables with the app context

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')  # Set host to 0.0.0.0 for Docker
