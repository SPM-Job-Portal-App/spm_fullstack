from flask import jsonify, request, Blueprint
import csv

from models.model import db;
from models.role import Role;

from role.roleService import RoleService;
role_bp = Blueprint('role', __name__)




@role_bp.route('/',methods=['GET'])
def get_roles():
    # import the roles from the csv file
    RoleService.importRoles();
    roles= Role.query.all()
    print(roles)
    if len(roles):
        return jsonify(
            {
                "code": 200,
                "roles": [role.json() for role in roles]
                
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no crops."
        }
    ), 404

