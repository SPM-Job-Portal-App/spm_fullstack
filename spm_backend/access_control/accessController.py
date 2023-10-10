from flask import jsonify, Blueprint
from access_control.accessService import AccessService
access_bp = Blueprint('access', __name__)

# Get role skills by role_name
@access_bp.route('/get_access')
def get_all_skills():
    try:
        AccessService.import_access()
        response = AccessService.get_all_access()
        return response, 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


