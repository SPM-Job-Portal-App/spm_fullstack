from flask import jsonify, request, Blueprint
from role_application.applicationService import Application
application_bp = Blueprint('application', __name__)

# apply for role listing
@application_bp.route('', methods=['POST'])
def apply_for_role_listing():
    data = request.get_json()
    try:
        response, status_code = Application.apply_for_role(data)
        return response, status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# read role application by staff ID
@application_bp.route('/<int:id>', methods=['GET'])
def get_role_listing(id):
    try:
        response, status_code = Application.get_role_listing_by_staff_id_application(id)
        return response, status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500