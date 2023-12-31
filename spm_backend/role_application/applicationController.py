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
def get_role_application(id):
    try:
        response, status_code = Application.get_role_listing_by_staff_id_application(id)
        return response, status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# read role applications
@application_bp.route('', methods=['GET'])
def get_role_applications():
    try:
        return jsonify(Application.get_role_applications(), 200)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# get applicants for a role_listing
@application_bp.route('/get_applicants/<int:role_listing_id>', methods=['GET'])
def get_applicants(role_listing_id):
    try:
        response, status_code = Application.get_role_application_by_listing_id(role_listing_id)
        return response, status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
# read role applications for all role listings, open and closed
@application_bp.route('/getapplications', methods=['GET'])
def get_role_applications_for_all_listings():
    try:
        return jsonify(Application.get_role_applications_for_all_listings(), 200)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# delete role application
@application_bp.route('', methods=['DELETE'])
def delete_role_application():
    data = request.get_json()
    try:
        response, status_code = Application.delete_role_application(data)
        return response, status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
