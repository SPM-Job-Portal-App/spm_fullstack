from flask import jsonify, Blueprint
from skill.skillService import SkillService
skill_bp = Blueprint('skill', __name__)

# Get role skills by role_name
@skill_bp.route('/get_skills')
def get_all_skills():
    try:
        SkillService.import_skills()
        response = SkillService.get_all_skills()
        return response, 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

