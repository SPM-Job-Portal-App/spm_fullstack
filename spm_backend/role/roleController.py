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
