import pytest
from main import app, drop_tables, initialize_databases
from models.model import db
from models.role_listing_model import RoleListing
from models.staff_model import Staff
from models.role_model import Role
from models.skill_model import Skill
from models.role_skill_model import RoleSkill

# Set up the Flask app for testing
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_apply_for_open_role_listing_success(client):
    initialize_databases()
    new_staff = Staff(
        staff_first_name="John",
        staff_last_name="Doe",
        dept="Engineering",
        country="USA",
        email="john.doe@example.com",
        role="Engineer"
    )
    new_role = Role(
        role_name="Software Engineer",
        role_description="Write code all day everyday. Write code all day everyday. Write code all day everyday."
    )
    new_skill = Skill(
        skill_name="Applications Development",
        skill_description="Develop applications based on the design specifications"
    )
    new_role_skill = RoleSkill(
        role_name="Software Engineer",
        skill_name="Applications Development"
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
        db.session.add(new_listing)
        db.session.add(new_role)
        db.session.add(new_skill)
        db.session.add(new_role_skill)
        db.session.commit()
        
    response = client.post('/application', json=application_data)
    expected_message = {'message': 'Role application created successfully'}
    assert response.json == expected_message
    assert response.status_code == 201
    drop_tables()

def test_apply_for_closed_role_listing_failure(client):
    initialize_databases()
    new_staff = Staff(
        staff_first_name="John",
        staff_last_name="Doe",
        dept="Engineering",
        country="USA",
        email="john.doe@example.com",
        role="Engineer"
    )
    new_role = Role(
        role_name="Software Engineer",
        role_description="Write code all day everyday. Write code all day everyday. Write code all day everyday."
    )
    new_skill = Skill(
        skill_name="Applications Development",
        skill_description="Develop applications based on the design specifications"
    )
    new_role_skill = RoleSkill(
        role_name="Software Engineer",
        skill_name="Applications Development"
    )
    new_listing = RoleListing(
        role_name="Software Engineer",
        country="USA",
        dept="Engineering",
        is_open=False,
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
        db.session.add(new_listing)
        db.session.add(new_role)
        db.session.add(new_skill)
        db.session.add(new_role_skill)
        db.session.commit()
    response = client.post('/application', json=application_data)
    expected_message = {'message': 'Application is closed'}
    assert response.json == expected_message
    assert response.status_code == 400
    drop_tables()

def test_apply_for_nonexistent_role_listing_failure(client):
    initialize_databases()
    new_staff = Staff(
        staff_first_name="John",
        staff_last_name="Doe",
        dept="Engineering",
        country="USA",
        email="john.doe@example.com",
        role="Engineer"
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
    new_staff = Staff(
        staff_first_name="John",
        staff_last_name="Doe",
        dept="Engineering",
        country="USA",
        email="john.doe@example.com",
        role="Engineer"
    )
    new_role = Role(
        role_name="Software Engineer",
        role_description="Write code all day everyday. Write code all day everyday. Write code all day everyday."
    )
    new_skill = Skill(
        skill_name="Applications Development",
        skill_description="Develop applications based on the design specifications"
    )
    new_role_skill = RoleSkill(
        role_name="Software Engineer",
        skill_name="Applications Development"
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
        db.session.add(new_listing)
        db.session.add(new_role)
        db.session.add(new_skill)
        db.session.add(new_role_skill)
        db.session.commit()
    with app.app_context():
        db.session.add(new_staff)
        db.session.add(new_listing)
        db.session.commit()
    client.post('/application', json=application_data)
    response = client.post('/application', json=application_data)
    expected_message = {'message': 'You have already applied for this role listing'}
    assert response.json == expected_message
    assert response.status_code == 400
    drop_tables()