import pytest
from main import app
from models.model import db


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def initialize_databases():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    initialize_databases()
    # Run all tests in the 'tests/' directory
    pytest.main(['tests/'])
