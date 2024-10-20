from models.agent_model import Agent
from models.feedback_model import Feedback

class MatchService:
    def __init__(self, db_session):
        self.db_session = db_session

    def match_agent(self, user_id):
        # Example logic to match an agent based on user feedback
        feedbacks = self.db_session.query(Feedback).filter_by(user_id=user_id).all()
        if not feedbacks:
            return None  # No feedback found for user

        agent_ids = [feedback.agent_id for feedback in feedbacks]
        agents = self.db_session.query(Agent).filter(Agent.id.in_(agent_ids)).all()
        return agents

    def get_all_agents(self):
        return self.db_session.query(Agent).all()
