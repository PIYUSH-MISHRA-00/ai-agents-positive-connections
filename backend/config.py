from flask_pymongo import PyMongo

mongo = PyMongo()

def initialize_db(app):
    app.config["MONGO_URI"] = "mongodb://localhost:27017/ai_agents"
    mongo.init_app(app)
