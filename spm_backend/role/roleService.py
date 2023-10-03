from models.model import db;
from models.role import Role;
from flask import jsonify;
import csv

class RoleService():

    def importRoles():
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


    

