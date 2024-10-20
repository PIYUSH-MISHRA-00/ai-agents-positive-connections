from config import mongo

class Feedback:
    def __init__(self, user_id, agent_id, rating, comments):
        self.user_id = user_id
        self.agent_id = agent_id
        self.rating = rating
        self.comments = comments

    def save(self):
        feedback = {
            "user_id": self.user_id,
            "agent_id": self.agent_id,
            "rating": self.rating,
            "comments": self.comments
        }
        return mongo.db.feedback.insert_one(feedback)
