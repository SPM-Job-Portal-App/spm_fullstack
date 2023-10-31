import pytest
from main import app, drop_tables, initialize_databases
from models.model import db
from models.staff_model import Staff
from models.role_model import Role

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_database_connection(client):
    initialize_databases()
    client.get('/access/get_access')
    new_staff = Staff(
        id = 130001,
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
    application_data = {
        "role_name": "Product Manager",
        "country": "USA",
        "dept": "Sales",
        "is_open": True,
        "opening_date": "2023-10-01",
        "closing_date": "2023-10-15",
        "reporting_manager": None
    }
    with app.app_context():
        db.session.add(new_staff)
        db.session.add(new_role)
        db.session.commit()
    response = client.post('/listing/create', json=application_data)
    expected_message = {'message': 'Role Listing created successfully'}
    assert response.json == expected_message
    assert response.status_code == 201
    drop_tables()