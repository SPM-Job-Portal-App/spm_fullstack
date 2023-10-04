from flask import jsonify, Blueprint
from skill.skillService import SkillService
skill_bp = Blueprint('skill', __name__)

# Get role skills by role_name
@skill_bp.route('/get_skills')
def get_skills_by_role_name():
    try:
        response = SkillService.get_skills_by_role_name()
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

