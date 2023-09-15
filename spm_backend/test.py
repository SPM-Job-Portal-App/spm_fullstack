import pytest
from main import app, db, User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

@pytest.fixture
def cleanup_database():
    yield
    user1 = db.session.query(User).filter_by(username='test_user1').first()
    if user1:
        db.session.delete(user1)
        db.session.commit()

def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Hello world"

def test_get_users(client, cleanup_database):
    user1 = User(username='test_user1', email='test1@example.com')
    db.session.add(user1)
    db.session.commit()

    response = client.get('/users')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 4
    assert data[-1]['username'] == 'test_user1'
    assert data[-1]['email'] == 'test1@example.com'