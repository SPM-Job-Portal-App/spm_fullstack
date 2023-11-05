import pytest
from main import app, drop_tables, initialize_databases
from models.model import db
from models.staff_model import Staff
from models.role_listing_model import RoleListing
from models.role_model import Role


# Set up the Flask app for testing
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# Test for successful editing of role listing
def test_edit_role_listing_success(client):
    initialize_databases()
    client.get('/access/get_access')
    new_role = Role(
        role_name="Developer",
        role_description="I call the manager's assistance"
    )
    new_open_role_listing = RoleListing(
        role_name="Developer",
        country="USA",
        dept="Sales",
        is_open=True,
        opening_date="2023-10-01",
        closing_date="2023-10-15",
        reporting_manager=None
    )
    with app.app_context():
        db.session.add(new_role)
        db.session.add(new_open_role_listing)
        db.session.commit()
    updated_role_listing_data = {
        "role_name": "Developer",
        "country": "Singapore",
        "dept": "Sales",
        "is_open": True,
        "opening_date": "2023-10-01",
        "closing_date": "2023-10-15",
        "reporting_manager": None
    }
    response = client.put('/listing/1', json=updated_role_listing_data)
    expected_message = {'message': 'Role listing updated successfully'}
    assert response.json == expected_message
    assert response.status_code == 201
    drop_tables()


# Test for updating listing data with missing fields failure
def test_edit_role_listing_missing_fields_failure(client):
    initialize_databases()
    client.get('/access/get_access')
    new_staff = Staff(
        id=130001,
        staff_first_name="James",
        staff_last_name="Re",
        dept="Sales",
        country="USA",
        email="james.re@example.com",
        role=1
    )
    new_role = Role(
        role_name="Product Manager",
        role_description="I call the manager's assistance"
    )
    new_open_role_listing = RoleListing(
        role_name="Product Manager",
        country="USA",
        dept="Sales",
        is_open=True,
        opening_date="2023-10-01",
        closing_date="2023-10-15",
        reporting_manager=None
    )
    updated_role_listing_data = {
        "role_name": "Product Manager",
        "country": "Singapore",
        "dept": "Sales",
        "is_open": True,
        "opening_date": "2023-10-01",
        "reporting_manager": None
    }
    with app.app_context():
        db.session.add(new_staff)
        db.session.add(new_role)
        db.session.add(new_open_role_listing)
        db.session.commit()
    response = client.put('/listing/1', json=updated_role_listing_data)
    expected_message = {'message': 'Missing required fields'}
    assert response.json == expected_message
    assert response.status_code == 400
    drop_tables()


# Test for updating nonexistent role listing
def test_edit_nonexistent_role_listing_failure(client):
    initialize_databases()
    client.get('/access/get_access')
    Staff(
        id=130001,
        staff_first_name="James",
        staff_last_name="Re",
        dept="Sales",
        country="USA",
        email="james.re@example.com",
        role=1
    )
    updated_role_listing_data = {
        "role_name": "Product Manager",
        "country": "Singapore",
        "dept": "Sales",
        "is_open": True,
        "opening_date": "2023-10-01",
        "closing_date": "2023-10-15",
        "reporting_manager": None
    }
    response = client.put('/listing/1', json=updated_role_listing_data)
    expected_message = {'message': 'Role listing at index does not exist'}
    assert response.json == expected_message
    assert response.status_code == 404
    drop_tables()


# Test for updating closed role lisiting
def test_edit_closed_role_listing_failure(client):
    initialize_databases()
    new_open_role_listing = RoleListing(
        role_name="Product Manager",
        country="USA",
        dept="Sales",
        is_open=False,
        opening_date="2023-10-01",
        closing_date="2023-10-15",
        reporting_manager=None
    )
    new_role = Role(
        role_name="Product Manager",
        role_description="I call the manager's assistance"
    )
    updated_role_listing_data = {
        "role_name": "Product Manager",
        "country": "Singapore",
        "dept": "Sales",
        "is_open": True,
        "opening_date": "2023-09-01",
        "closing_date": "2023-10-03",
        "reporting_manager": None
    }
    with app.app_context():
        db.session.add(new_open_role_listing)
        db.session.add(new_role)
        db.session.commit()
    response = client.put('/listing/1', json=updated_role_listing_data)
    expected_message = {'message': "Role listing at index is already closed"}
    assert response.json == expected_message
    assert response.status_code == 400
    drop_tables()
