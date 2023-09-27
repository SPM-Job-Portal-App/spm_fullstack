# import pytest
# from flask import Flask

# from main import app

# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     client = app.test_client()
#     yield client

# def test_connection(client):
#     response = client.get('/')
#     assert response.status_code == 200
# def test_create_role_listings(client):
#     # Create the  role listing from the 
    
#     response = client.post('/role/')
#     assert response.status_code ==201
#     response = client.get('/role/')
#     assert response.status_code == 200
    
   
#     response = response.json
#     assert response['roles'][0]['label'] == "Software Developer"
#     assert response['roles'][0]['skill'] =="Software Development"
#     assert response['roles'][0]['description'] =='Programme Software Products'
#     assert response['roles'][0]['department'] =='Engineering'


    