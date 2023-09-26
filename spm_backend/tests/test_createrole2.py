import json
import pytest
from main import app, db
from models import RoleListing

@pytest.fixture
def client():
    # Create a test client using Flask's test_client
    app.config['TESTING'] = True
    client = app.test_client()

    # Set up a test database (SQLite in memory) for testing
    with app.app_context():
        db.create_all()

    yield client

    # Clean up the test database after testing
    # with app.app_context():
    #     db.drop_all()

def test_create_role_listing(client):
    # Define a sample role listing data for testing
    data = {
        "role_name": "Software Engineer",
        "skills": "Python, Flask",
        "country": "USA",
        "dept": "Engineering",
        "is_open": True,
        "reporting_manager": 1
    }

    # Send a POST request to create the role listing
    response = client.post('/listing/create', data=json.dumps(data), content_type='application/json')

    # Check the response status code and content
    assert response.status_code == 201  # 201 Created
    assert b"Role Listing created successfully" in response.data

    # Verify that the role listing was added to the database
    with app.app_context():
        role_listing = RoleListing.query.filter_by(role_name=data["role_name"]).first()
        assert role_listing is not None
        assert role_listing.skills == data["skills"]
        assert role_listing.country == data["country"]
        assert role_listing.dept == data["dept"]
        assert role_listing.is_open == data["is_open"]
        assert role_listing.reporting_manager == data["reporting_manager"]



def test_create_duplicate_role_listing(client):
    # Define a sample role listing data for testing
    data = {
        "role_name": "Software Engineer",
        "skills": "Python, Flask",
        "country": "USA",
        "dept": "Engineering",
        "is_open": True,
        "reporting_manager": 1
    }

    # Send a POST request to create the role listing
    response = client.post('/listing/create', data=json.dumps(data), content_type='application/json')

    # Check the response status code and content
    assert response.status_code == 409  # 409 Conflict
    assert b"Role Listing already exists" in response.data
    
    
def test_create_role_listing_empty_fields(client):
    # Define a sample role listing data with empty fields for testing
    data = {
        "role_name": "",  # Empty field
        "skills": "Python, Flask",
        "country": "USA",
        "dept": "",  # Empty field
        "is_open": True,
        "reporting_manager": "John Doe"
    }

    # Send a POST request to create the role listing
    response = client.post('/listing/create', data=json.dumps(data), content_type='application/json')

    # Check the response status code and content
    assert response.status_code == 400  # 400 Bad Request
    assert b"Missing required fields" in response.data