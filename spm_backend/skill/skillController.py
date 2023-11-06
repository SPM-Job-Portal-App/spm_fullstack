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

# Get role skills by role_name
@skill_bp.route('/get_skill_by_skill_name/<skill_name>')
def get_skill_by_skill_name(skill_name):
    try:
        response = SkillService.get_skill_by_skill_name(skill_name)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error with skill': str(e)}), 500

