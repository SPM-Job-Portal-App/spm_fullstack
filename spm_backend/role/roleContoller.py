from flask import jsonify, request, Blueprint

from models.role_model import Role;
from role.roleService import RoleService;
role_bp = Blueprint('role', __name__)

@role_bp.route('/',methods=['GET'])
def get_roles():
    # import the roles from the csv file
    RoleService.importRoles()
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
            "message": "There are no roles."
        }
    ), 404


@role_bp.route('/get_role_by_role_name/<role_name>')
def get_role_by_role_name(role_name):
    try:
        response = RoleService.get_role_by_role_name(role_name)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

