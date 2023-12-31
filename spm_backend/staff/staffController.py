from flask import jsonify, request, Blueprint
from staff.staffService import StaffService
staff_bp = Blueprint('staff', __name__)

# Get staff by id
@staff_bp.route('/get_staff_by_id/<id>')
def get_staff_by_id(id):
    try:
        response = StaffService.get_staff_by_id(id)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@staff_bp.route('/get_staff')
def get_all_skills():

    StaffService.importRoleSkill()
    response = StaffService.get_all_staff()
    return response, 200
