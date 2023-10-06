from flask import jsonify, Blueprint
from role.roleService import RoleService
role_bp = Blueprint('role', __name__)

# Get a role by role_name
@role_bp.route('/get_role_by_role_name/<role_name>')
def get_role_by_role_name(role_name):
    try:
        response = RoleService.get_role_by_role_name(role_name)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Get all the roles
@role_bp.route('/get_all_role_names', methods=['GET'])
def get_all_role_names():
    try:
        response = RoleService.get_all_role_names()
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
