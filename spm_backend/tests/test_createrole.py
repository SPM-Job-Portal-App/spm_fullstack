# import pytest
# from main import app, drop_tables, initialize_databases
# from models.model import db
# from models.role_listing_model import RoleListing
# from models.staff_model import Staff

# # Set up the Flask app for testing
# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     with app.test_client() as client:
#         yield client

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
#     application_data = {
#         "role_listing": 1,
#         "staff_id": 1
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