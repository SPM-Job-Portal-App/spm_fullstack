import pytest
from main import app, drop_tables, initialize_databases
from models.model import db
from models.role_listing_model import RoleListing
from models.staff_model import Staff
from models.role_model import Role
from models.role_skill_model import RoleSkill
from models.skill_model import Skill

# Set up the Flask app for testing
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_close_open_role_listing(client):
    initialize_databases()
    client.get('/access/get_access')

    with app.app_context():

        new_staff = Staff(
            id = 130001,
            staff_first_name="Alice",
            staff_last_name="Smith",
            dept="Engineering",
            country="Canada",
            email="alice.smith@example.com",
            role=1
        )
        db.session.add(new_staff)
        db.session.commit()

        new_skill = Skill(
                skill_name="Applications Development",
                skill_desc="Develop applications based on the design specifications"
            )
        db.session.add(new_skill)
        db.session.commit()

        new_role = Role(
                role_name="Developer",
                role_description="Write code all day everyday. Write code all day everyday. Write code all day everyday."
            )
        db.session.add(new_role)
        db.session.commit()

        new_role_skill = RoleSkill(
                role_name="Developer",
                skill_name="Applications Development"
            )
        db.session.add(new_role_skill)
        db.session.commit()

        new_listing = RoleListing(
                role_name="Developer",
                country="Canada",
                dept="IT",
                is_open=True,
                reporting_manager=130001,
                opening_date="2023-10-01",
                closing_date="2023-12-15"
            )
        db.session.add(new_listing)
        db.session.commit()

    response = client.put('/listing/close_role_listing/1')

    response_data = response.get_json()
    # check all fields are correct
    expected_message = "Role listing with id 1 closed successfully"

    assert response_data[0]["message"] == expected_message
  
    drop_tables()


def test_close_closed_role_listing(client):
    initialize_databases()
    client.get('/access/get_access')

    with app.app_context():

        new_staff = Staff(
            id = 130001,
            staff_first_name="Alice",
            staff_last_name="Smith",
            dept="Engineering",
            country="Canada",
            email="alice.smith@example.com",
            role=1
        )
        db.session.add(new_staff)
        db.session.commit()

        new_skill = Skill(
                skill_name="Applications Development",
                skill_desc="Develop applications based on the design specifications"
            )
        db.session.add(new_skill)
        db.session.commit()

        new_role = Role(
                role_name="Developer",
                role_description="Write code all day everyday. Write code all day everyday. Write code all day everyday."
            )
        db.session.add(new_role)
        db.session.commit()

        new_role_skill = RoleSkill(
                role_name="Developer",
                skill_name="Applications Development"
            )
        db.session.add(new_role_skill)
        db.session.commit()

        new_listing = RoleListing(
                role_name="Developer",
                country="Canada",
                dept="IT",
                is_open=False,
                reporting_manager=130001,
                opening_date="2023-10-01",
                closing_date="2023-12-15"
            )
        db.session.add(new_listing)
        db.session.commit()

    response = client.put('/listing/close_role_listing/1')

    response_data = response.get_json()
    # check all fields are correct
    expected_message = {"error": "Listing with id 1 already closed and so cannot be closed again!"}

    assert response_data == expected_message
  
    drop_tables()

