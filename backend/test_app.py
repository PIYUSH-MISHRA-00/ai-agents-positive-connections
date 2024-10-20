import pytest
from app import app, db
from models.agent_model import Agent
from models.feedback_model import Feedback

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use an in-memory database for testing
    with app.app_context():
        db.create_all()  # Create tables
        yield app.test_client()
        db.drop_all()  # Clean up after tests

def test_get_agents(client):
    response = client.get('/api/agents')
    assert response.status_code == 200
    assert response.json == []

    # Adding a sample agent for further testing
    new_agent = Agent(name='Test Agent', specialty='Test Specialty')
    db.session.add(new_agent)
    db.session.commit()

    response = client.get('/api/agents')
    assert len(response.json) == 1
    assert response.json[0]['name'] == 'Test Agent'

def test_submit_feedback(client):
    # Prepare an agent for the feedback test
    new_agent = Agent(name='Test Agent', specialty='Test Specialty')
    db.session.add(new_agent)
    db.session.commit()

    response = client.post('/api/feedback', json={
        'agent_id': new_agent.id,
        'user_feedback': 'Great service!'
    })
    assert response.status_code == 201
    assert response.json['user_feedback'] == 'Great service!'
