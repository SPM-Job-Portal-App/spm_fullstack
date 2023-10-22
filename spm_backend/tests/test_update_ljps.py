import pytest
from main import app, drop_tables, initialize_databases
from models.model import db
from models.role_model import Role
import csv


# Set up the Flask app for testing
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_import_role_desc(client):
    initialize_databases()
    
    #Check if the role is imported from the csv file properly and check wit the get request
    #iterate over every role and check the content match the csv file
    
    json_response = client.get('/role/').get_json()
    with open('./role/role.csv', newline='', encoding='utf-8-sig',errors='replace') as csv_file:
        csvreader = csv.DictReader(csv_file)
        # Iterate through the CSV file and JSON data together
        for csv_item, json_item in zip(csvreader, json_response['roles']):
            # Here, you can compare individual fields or attributes of the JSON and CSV items.
            assert json_item['Role'] == csv_item['Role_name'], "Role Name doesn't match."
            assert json_item['Role Description'] == csv_item['Role_Desc'], "Role description doesn't match."
    
def test_import_skill_desc(client):
    initialize_databases()
    
    #Check if the role is imported from the csv file properly and check wit the get request
    #iterate over every role and check the content match the csv file
    json_response = client.get('/skill/get_skills').get_json()
    with open('./skill/skill.csv', newline='', encoding='utf-8-sig',errors='replace') as csv_file:
        csvreader = csv.DictReader(csv_file)
        print(json_response)
        # Iterate through the CSV file and JSON data together
        for csv_item, json_item in zip(csvreader, json_response['skills']):
            # Here, you can compare individual fields or attributes of the JSON and CSV items.
            assert json_item['Skill Name'] == csv_item['Skill_Name'], "Role name doesn't match."
            assert json_item['Skill Description'] == csv_item['Skill_Desc'], "Role description doesn't match."
    
def test_import_role_skill(client):
    initialize_databases()
    
    #Check if the role is imported from the csv file properly and check wit the get request
    #iterate over every role and check the content match the csv file
    json_response = client.get('/roleskill/get_skills').get_json()
    with open('./role_skill/role_skill.csv', newline='', encoding='utf-8-sig',errors='replace') as csv_file:
        csvreader = csv.DictReader(csv_file)
        print(json_response)
        # Iterate through the CSV file and JSON data together
        for csv_item, json_item in zip(csvreader, json_response['skills']):
            # Here, you can compare individual fields or attributes of the JSON and CSV items.
            assert json_item['Role Name'] == csv_item['Role_Name'], "Role Name doesn't match."
            assert json_item['Skill Name'] == csv_item['Skill_Name'], "Skill Name doesn't match."
    drop_tables()

def test_import_access_control(client):
    initialize_databases()
    
    #Check if the role is imported from the csv file properly and check wit the get request
    #iterate over every role and check the content match the csv file
    json_response = client.get('/access/get_access').get_json()
    with open('./access_control/access_control.csv', newline='', encoding='utf-8-sig',errors='replace') as csv_file:
        csvreader = csv.DictReader(csv_file)
        print(json_response)
        # Iterate through the CSV file and JSON data together
        for csv_item, json_item in zip(csvreader, json_response['Access']):
            # Here, you can compare individual fields or attributes of the JSON and CSV items.
            print(csv_item)
            print(json_item)
            assert json_item['Access Id'] == int(csv_item['Access_ID']), "Access Id does not match"
            assert json_item['Access Control Name'] == csv_item['Access_Control_Name'], "Access Control Name doesn't match."
def test_import_staff(client):
    initialize_databases()
    
    #Check if the role is imported from the csv file properly and check wit the get request
    #iterate over every role and check the content match the csv file
    json_response = client.get('/staff/get_staff').get_json()
    with open('./staff/staff.csv', newline='', encoding='utf-8-sig',errors='replace') as csv_file:
        csvreader = csv.DictReader(csv_file)
        print(json_response)
        # Iterate through the CSV file and JSON data together
        for csv_item, json_item in zip(csvreader, json_response['staff']):
            # Here, you can compare individual fields or attributes of the JSON and CSV items.
            print(csv_item)
            print(json_item)
            assert json_item['Staff Id'] == int(csv_item['Staff_ID']), "Staff Id does not match"
         
def test_import_staff_skill(client):
    initialize_databases()
    
    #Check if the role is imported from the csv file properly and check wit the get request
    #iterate over every role and check the content match the csv file
    json_response = client.get('/skill/get_skills').get_json()
    json_response = client.get('/staffskill/get_skills').get_json()
    with open('./staff_skill/staff_skill.csv', newline='', encoding='utf-8-sig',errors='replace') as csv_file:
        csvreader = csv.DictReader(csv_file)
        print(json_response)
        # Iterate through the CSV file and JSON data together
        for csv_item, json_item in zip(csvreader, json_response['skills']):
            # Here, you can compare individual fields or attributes of the JSON and CSV items.
          
            assert json_item['Staff Id'] == int(csv_item['Staff_ID']), "Staff Id does not match"
            assert json_item['Skill Name '] == csv_item['Skill_Name'], "Staff Id does not match"
    drop_tables()
         
    







