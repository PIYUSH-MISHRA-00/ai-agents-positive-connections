from models.feedback_model import Feedback

class FeedbackService:
    def __init__(self, db_session):
        self.db_session = db_session

    def submit_feedback(self, agent_id, user_feedback):
        new_feedback = Feedback(agent_id=agent_id, user_feedback=user_feedback)
        self.db_session.add(new_feedback)
        self.db_session.commit()
        return new_feedback
