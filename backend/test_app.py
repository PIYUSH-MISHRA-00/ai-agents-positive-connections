# backend/test_app.py
import pytest
from app import app, db
from models.user_model import User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up the database after tests

def test_create_user(client):
    response = client.post('/users', json={
        'name': 'Jane Doe',
        'email': 'jane@example.com',
        'interests': 'Web Development, Python'
    })
    assert response.status_code == 200
    assert b'User created' in response.data

def test_fetch_users(client):
    client.post('/users', json={
        'name': 'Jane Doe',
        'email': 'jane@example.com',
        'interests': 'Web Development, Python'
    })
    response = client.get('/users')
    assert response.status_code == 200
    assert b'Jane Doe' in response.data
