from config import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    interests = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<User {self.name}>'
