from flask import jsonify, Blueprint
from staff_skill.staffSkillService import StaffSkillService
staff_skill_bp = Blueprint('staff_skill', __name__)

# Get role skills by role_name
@staff_skill_bp.route('/get_skills')
def get_all_skills():
    try:
        StaffSkillService.import_skills()
        response = StaffSkillService.get_all_skills()
        return response, 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Get all staff_skills of a staff with staff_id
@staff_skill_bp.route('/get_staff_skills/<int:id>')
def get_staff_skills(id):
    try:
        response = StaffSkillService.get_staff_skills(id)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500