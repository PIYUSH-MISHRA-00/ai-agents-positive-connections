from app import db

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'), nullable=False)
    user_feedback = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'agent_id': self.agent_id,
            'user_feedback': self.user_feedback
        }
