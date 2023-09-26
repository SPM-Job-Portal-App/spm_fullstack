from main import app, db
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://user:password@localhost:3306/db'
    client = app.test_client()
    with app.app_context():
        db.create_all()
    yield client
    with app.app_context():
        db.drop_all()

def test_create_role_listing_missing_fields(client):
    # Test with missing required fields
    data = {
        'role_name': 'Test Role',
        'country': 'USA',
        'dept': 'HR',
        'is_open': True,
        'reporting_manager': 1
    }

    response = client.post('/listing/create', json=data)
    data = response.get_json()

    assert response.status_code == 400
    assert "required but missing" in data['message']

def test_create_role_listing_empty_fields(client):
    # Test with empty fields
    data = {
        'role_name': 'Test Role',
        'skills': '',
        'country': 'USA',
        'dept': 'HR',
        'is_open': True,
        'reporting_manager': 1
    }

    response = client.post('/listing/create', json=data)
    data = response.get_json()

    assert response.status_code == 400
    assert "cannot be empty" in data['message']

def test_create_role_listing_valid_input(client):
    # Test with valid input
    data = {
        'role_name': 'Test Role',
        'skills': 'Skill 1',
        'country': 'USA',
        'dept': 'HR',
        'is_open': True,
        'reporting_manager': 1
    }

    response = client.post('/listing/create', json=data)
    data = response.get_json()

    assert response.status_code == 201
    assert data['message'] == 'Role Listing created successfully'
