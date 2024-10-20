from config import app, db
from routes.users import user_bp
from routes.agents import agent_bp
from routes.feedback import feedback_bp

# Register Blueprints
app.register_blueprint(user_bp)
app.register_blueprint(agent_bp)
app.register_blueprint(feedback_bp)

# Create tables
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
