import pytest
from flask import Flask

from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_apply_for_open_role_listing(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Flask API works!"