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

def test_get_open_role_listings(client):
    initialize_databases()

    with app.app_context():

        new_staff = Staff(
            staff_first_name="John",
            staff_last_name="Doe",
            dept="Engineering",
            country="USA",
            email="john.doe@example.com",
            role="Engineer"
        )
        db.session.add(new_staff)
        db.session.commit()

        new_listing = RoleListing(
                role_name="Software Engineer",
                skills="Python, JavaScript, SQL",
                country="USA",
                dept="Engineering",
                is_open=True,
                reporting_manager=1
            )
        db.session.add(new_listing)
        db.session.commit()

    response = client.get('/listing/get_open_listings')
    expected_result = [
        {
            "country": "USA",
            "dept": "Engineering",
            "id": 1,
            "is_open": True,
            "reporting_manager": "John Doe",
            "role_name": "Software Engineer",
            "skills": "Python, JavaScript, SQL"
        }
    ]

    response_data = response.json
    # check all fields are correct
    assert response_data[0]['country'] == expected_result[0]['country']
    assert response_data[0]['dept'] == expected_result[0]['dept']
    assert response_data[0]['is_open'] == expected_result[0]['is_open']
    assert response_data[0]['reporting_manager'] == expected_result[0]['reporting_manager']
    assert response_data[0]['role_name'] == expected_result[0]['role_name']
    assert response_data[0]['skills'] == expected_result[0]['skills']
    drop_tables()


def test_get_closed_role_listings(client):
    initialize_databases()

    with app.app_context():

        new_staff = Staff(
            staff_first_name="John",
            staff_last_name="Doe",
            dept="Engineering",
            country="USA",
            email="john.doe@example.com",
            role="Engineer"
        )
        db.session.add(new_staff)
        db.session.commit()

        new_listing = RoleListing(
                role_name="Software Engineer",
                skills="Python, JavaScript, SQL",
                country="USA",
                dept="Engineering",
                is_open=False,
                reporting_manager=1
            )
        db.session.add(new_listing)
        db.session.commit()

    response = client.get('/listing/get_open_listings')
    expected_message = [{'message': 'No open role listings'}, 404]
    assert response.json == expected_message
    
    drop_tables()

    