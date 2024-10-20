from config import mongo

class Agent:
    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise

    def save(self):
        agent = {
            "name": self.name,
            "expertise": self.expertise
        }
        return mongo.db.agents.insert_one(agent)
