from flask import jsonify, request, Blueprint
import csv
from role.role import Role
from models import db;


role_bp = Blueprint('role', __name__)


@role_bp.route('/',methods=['POST'])
def update_role():
    with open('./role/role_skill.csv', newline='',encoding='utf-8-sig') as csv_file:
        csvreader = csv.DictReader(csv_file)
        
        for row in csvreader:
            print(row)
            new_role = Role(
                role_name=row['Role'],
                skill_name=row['Skill']
            )
            db.session.add(new_role)
        db.session.commit()
        
    return jsonify({'message': 'Roles Updated'}), 201
