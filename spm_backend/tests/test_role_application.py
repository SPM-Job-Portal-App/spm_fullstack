import pytest
from main import app, drop_tables, initialize_databases
from models.model import db
from models.role_listing_model import RoleListing
from models.role_application_model import RoleApplication
from models.staff_model import Staff
from models.role_model import Role

# Set up the Flask app for testing
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# role listing id exist and get applicants
def test_retrieve_applications_using_listing_id(client):
    initialize_databases()
    client.get('/access/get_access')
    
    new_staff = Staff(
        id = 130001,
        staff_first_name="John",
        staff_last_name="Doe",
        dept="Engineering",
        country="USA",
        email="john.doe@example.com",
        role=1
    )
    new_role = Role(
        role_name="Software Engineer",
        role_description="I call the manager's assistance"
    )
    new_listing = RoleListing(
        role_name="Software Engineer",
        country="USA",
        dept="Engineering",
        is_open=True,
        opening_date="2023-10-04",
        closing_date="2023-12-30",
        reporting_manager=None
    )
    new_role_application = RoleApplication(
        application_date = "2023-10-12",
        role_listing_id = 1,
        staff_id = 130001
    )
    with app.app_context():
        db.session.add(new_staff)
        db.session.add(new_role)
        db.session.add(new_listing)
        db.session.add(new_role_application)
        db.session.commit()
    # response = client.get('application/get_applicants/1')
    # retrieved_message = response["message"]
    # expected_message = "Applicants retrieved successfully"
    # assert retrieved_message == expected_message
    # drop_tables()
    
    # Make a test request using the client
    response = client.get('/application/get_applicants/1')
    
    # Check the HTTP status code
    assert response.status_code == 200 

    # Parse the response content using response.json()
    response_data = response.json

    # Now you can access specific data from the response_data dictionary
    retrieved_message = response_data.get("message", "")

    # Define the expected message
    expected_message = "Applicants retrieved successfully"

    # Perform your assertion on the retrieved message
    assert retrieved_message == expected_message
    drop_tables()

def test_apply_for_open_role_listing_success(client):
    initialize_databases()
    client.get('/access/get_access')

    new_staff = Staff(
        id = 130001,
        staff_first_name="John",
        staff_last_name="Doe",
        dept="Engineering",
        country="USA",
        email="john.doe@example.com",
        role=1
    )
    new_role = Role(
        role_name="Software Engineer",
        role_description="I call the manager's assistance"
    )
    new_listing = RoleListing(
        role_name="Software Engineer",
        country="USA",
        dept="Engineering",
        is_open=True,
        opening_date="2023-10-04",
        closing_date="2023-12-30",
        reporting_manager=None
    )
    application_data = {
        "role_listing": 1,
        "staff_id": 1
    }
    with app.app_context():
        db.session.add(new_staff)
        db.session.add(new_role)
        db.session.add(new_listing)
        db.session.commit()
        
    response = client.post('/application', json=application_data)
    expected_message = {'message': 'Role application created successfully'}
    assert response.json == expected_message
    assert response.status_code == 201
    drop_tables()

def test_apply_for_closed_role_listing_failure(client):
    initialize_databases()
    client.get('/access/get_access')
    
    new_listing = RoleListing(
        role_name="Software Engineer",
        country="USA",
        dept="Engineering",
        is_open=False,
        opening_date="2023-09-04",
        closing_date="2023-09-30",
        reporting_manager=None
    )
    new_role = Role(
        role_name="Software Engineer",
        role_description="I call the manager's assistance"
    )
    new_staff = Staff(
        id = 130001,
        staff_first_name="John",
        staff_last_name="Doe",
        dept="Engineering",
        country="USA",
        email="john.doe@example.com",
        role=1
    )
    application_data = {
        "role_listing": 1,
        "staff_id": 1
    }
    with app.app_context():
        db.session.add(new_listing)
        db.session.add(new_role)
        db.session.add(new_staff)
        db.session.commit()
    response = client.post('/application', json=application_data)
    expected_message = {'message': 'Application is closed'}
    assert response.json == expected_message
    assert response.status_code == 400
    drop_tables()

def test_apply_for_nonexistent_role_listing_failure(client):
    initialize_databases()
    client.get('/access/get_access')

    new_staff = Staff(
        id = 130001,
        staff_first_name="John",
        staff_last_name="Doe",
        dept="Engineering",
        country="USA",
        email="john.doe@example.com",
        role=1
    )
    application_data = {
        "role_listing": 1,
        "staff_id": 1
    }
    with app.app_context():
        db.session.add(new_staff)
        db.session.commit()
    response = client.post('/application', json=application_data)
    expected_message = {'message': 'Role listing at index does not exist'}
    assert response.json == expected_message
    assert response.status_code == 404
    drop_tables()

def test_apply_for_role_listing_with_active_application_failure(client):
    initialize_databases()
    client.get('/access/get_access')

    new_staff = Staff(
        id = 130001,
        staff_first_name="John",
        staff_last_name="Doe",
        dept="Engineering",
        country="USA",
        email="john.doe@example.com",
        role=1
    )
    new_role = Role(
        role_name="Software Engineer",
        role_description="I call the manager's assistance"
    )
    new_listing = RoleListing(
        role_name="Software Engineer",
        country="USA",
        dept="Engineering",
        is_open=True,
        opening_date="2023-10-04",
        closing_date="2023-12-30",
        reporting_manager=None
    )
    application_data = {
        "role_listing": 1,
        "staff_id": 1
    }
    with app.app_context():
        db.session.add(new_staff)
        db.session.add(new_role)
        db.session.add(new_listing)
        db.session.commit()
    client.post('/application', json=application_data)
    response = client.post('/application', json=application_data)
    expected_message = {'message': 'You have already applied for this role listing'}
    assert response.json == expected_message
    assert response.status_code == 400
    drop_tables()