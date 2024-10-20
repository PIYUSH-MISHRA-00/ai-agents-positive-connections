from config import db

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    expertise = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Agent {self.name}>"
