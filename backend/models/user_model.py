from config import mongo

class User:
    def __init__(self, name, email, interests):
        self.name = name
        self.email = email
        self.interests = interests

    def save(self):
        user = {
            "name": self.name,
            "email": self.email,
            "interests": self.interests
        }
        return mongo.db.users.insert_one(user)
