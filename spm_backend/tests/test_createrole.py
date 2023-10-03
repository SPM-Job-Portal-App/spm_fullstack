import pytest
from main import app, drop_tables, initialize_databases
from models.model import db
from models.role_listing_model import RoleListing
from models.staff_model import Staff

# Set up the Flask app for testing
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Initialize the database before testing
@pytest.fixture(autouse=True)
def setup_database():
    with app.app_context():
        initialize_databases()
        yield  # The test will run here
        db.session.remove()
        db.drop_all()
        
# Test for successful creation of role listing 
def test_create_success(client):
    new_staff = Staff(
        staff_first_name="James",
        staff_last_name="Re",
        dept="Sales",
        country="USA",
        email="james.re@example.com",
        role="Product Manager"
    )
    application_data = {
        "role_name": "Product Manager",
        "skills": "Python, JavaScript, SQL",
        "country": "USA",
        "dept": "Sales",
        "is_open": True,
        "reporting_manager": None
    }
    with app.app_context():
        db.session.add(new_staff)
        db.session.commit()
    response = client.post('/listing/create', json=application_data)
    expected_message = {'message': 'Role Listing created successfully'}
    assert response.json == expected_message
    assert response.status_code == 201

# Test for creating a duplicate role listing which already exists in the database
def test_create_duplicate_roles(client):
    new_staff = Staff(
        staff_first_name="James",
        staff_last_name="Re",
        dept="Sales",
        country="USA",
        email="james.re@example.com",
        role="Product Manager"
    )
    application_data = {
        "role_name": "Product Manager",
        "skills": "Python, JavaScript, SQL",
        "country": "USA",
        "dept": "Sales",
        "is_open": True,
        "reporting_manager": None
    }
    duplicate_data = {
        "role_name": "Product Manager",
        "skills": "Python, JavaScript, SQL",
        "country": "USA",
        "dept": "Sales",
        "is_open": True,
        "reporting_manager": None
    }
    with app.app_context():
        db.session.add(new_staff)
        db.session.commit()
    # Send the first POST request
    response1 = client.post('/listing/create', json=application_data)
    expected_message1 = {'message': 'Role Listing created successfully'}
    assert response1.json == expected_message1
    assert response1.status_code == 201

    # Send the second POST request with duplicate data
    response2 = client.post('/listing/create', json=duplicate_data)
    expected_message2 = {'message': 'Role Listing already exists'}
    assert response2.json == expected_message2
    assert response2.status_code == 409

# Test for creating a role listing with an empty field
def test_create_role_empty_fields(client):
    new_staff = Staff(
        staff_first_name="James",
        staff_last_name="Re",
        dept="Sales",
        country="USA",
        email="james.re@example.com",
        role="Product Manager"
    )
    application_data = {
        "role_name": "",
        "skills": "Python, JavaScript, SQL",
        "country": "USA",
        "dept": "Sales",
        "is_open": True,
        "reporting_manager": None
    }
    with app.app_context():
        db.session.add(new_staff)
        db.session.commit()
    # Send the first POST request
    response = client.post('/listing/create', json=application_data)
    expected_message = {'message': 'Missing required fields'}
    assert response.json == expected_message
    assert response.status_code == 400


##################################################################################################### 
# def test_create_happy_path(client):
#     initialize_databases()
#     new_listing = RoleListing(
#         role_name="Product Manager",
#         skills="Python, JavaScript, SQL",
#         country="USA",
#         dept="Sales",
#         is_open=True,
#         reporting_manager=None
#     )
#     new_staff = Staff(
#         staff_first_name="James",
#         staff_last_name="Re",
#         dept="Sales",
#         country="USA",
#         email="james.re@example.com",
#         role="Product Manager"
#     )
#     # application_data = {
#     #     "role_listing": 1,
#     #     "staff_id": 1
#     # }
#     application_data = {
#         "role_name": "Product Manager",
#         "skills": "Python, JavaScript, SQL",
#         "country": "USA",
#         "dept": "Sales",
#         "is_open": True,
#         "reporting_manager": None
#     }
#     with app.app_context():
#         db.session.add(new_listing)
#         db.session.add(new_staff)
#         db.session.commit()
#     response = client.post('/listing/create', json=application_data)
#     expected_message = {'message': 'Role Listing created successfully'}
#     assert response.json == expected_message
#     assert response.status_code == 201
#     drop_tables()