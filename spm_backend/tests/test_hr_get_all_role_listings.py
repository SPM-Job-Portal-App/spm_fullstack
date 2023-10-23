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

def test_get_all_role_listings(client):
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

        new_role2 = Role(
                role_name="Manager",
                role_description="Lead lead lead!"
            )
        db.session.add(new_role2)
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
                closing_date="2023-10-15" 
            )
        db.session.add(new_listing)
        db.session.commit()

        new_listing2 = RoleListing(
                role_name="Manager",
                country="Singapore",
                dept="IT",
                is_open=False,
                reporting_manager=130001,
                opening_date="2023-10-01",
                closing_date="2023-10-15" 
            )
        db.session.add(new_listing2)
        db.session.commit()

    response = client.get('/listing/get_all_listings')
    expected_result = [
        {
            "country": "Canada",
            "dept": "IT",
            "id": 1,
            "is_open": True,
            "reporting_manager": "Alice Smith",
            "role_name": "Developer",
        },
        {
            "country": "Singapore",
            "dept": "IT",
            "id": 2,
            "is_open": False,
            "reporting_manager": "Alice Smith",
            "role_name": "Manager",
        }
    ]

    response_data = response.get_json()

    # check all fields are correct
    assert response_data[0]['country'] == expected_result[0]['country']
    assert response_data[0]['dept'] == expected_result[0]['dept']
    assert response_data[0]['is_open'] == expected_result[0]['is_open']
    assert response_data[0]['reporting_manager'] == expected_result[0]['reporting_manager']
    assert response_data[0]['role_name'] == expected_result[0]['role_name']

    assert response_data[1]['country'] == expected_result[1]['country']
    assert response_data[1]['dept'] == expected_result[1]['dept']
    assert response_data[1]['is_open'] == expected_result[1]['is_open']
    assert response_data[1]['reporting_manager'] == expected_result[1]['reporting_manager']
    assert response_data[1]['role_name'] == expected_result[1]['role_name']

    drop_tables()


def test_get_all_role_listings_when_no_role_listing(client):
    initialize_databases()

    with app.app_context():
        client.get('/access/get_access')

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

    response = client.get('/listing/get_all_listings')
    expected_message = { "error": "No role listings" }
    assert response.json == expected_message
    
    drop_tables()

    