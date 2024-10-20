from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.agents import agents_bp
from routes.feedback import feedback_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Local SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Register Blueprints
app.register_blueprint(agents_bp)
app.register_blueprint(feedback_bp)

# Create the database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
