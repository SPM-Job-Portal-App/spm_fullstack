from models.model import db;
from models.role_model import Role;
from flask import jsonify;
import csv

class RoleService():

    def importRoles():
        existing_role_count = db.session.query(Role).count()
    
        if existing_role_count > 0:
            return 
        with open('./role/role.csv', newline='',encoding='utf-8-sig',errors='replace') as csv_file:
            csvreader = csv.DictReader(csv_file)
            
            for row in csvreader:
                print(row['Role_Desc'])
                new_role = Role(
                    role_name=row['Role_name'],
                    role_description=row['Role_Desc'],
                    
                )
                db.session.add(new_role)
            db.session.commit()
            
        return jsonify({'message': 'Roles Updated'}), 201


    def get_role_by_role_name(role_name_input):
        print(role_name_input)
        try:
            role_response = Role.query.filter(Role.role_name == role_name_input).first()

            role =  {
                'role_name': role_response.role_name,
                'role_desc': role_response.role_description
            }
            return role
        except Exception as e:
            raise Exception("No role with this role name found")
        
    def get_all_role_names():
        try:
            # Query all roles and retrieve only the role names
            roles = Role.query.with_entities(Role.role_name).all()

            # Extract role names from the query result
            role_names = [role[0] for role in roles]

            return role_names
        except Exception as e:
            raise Exception("An error occurred while retrieving role names")

