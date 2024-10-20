from config import db

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)  # Assuming foreign key to User
    agent_id = db.Column(db.Integer, nullable=False)  # Assuming foreign key to Agent
    comment = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Feedback {self.comment}>"
