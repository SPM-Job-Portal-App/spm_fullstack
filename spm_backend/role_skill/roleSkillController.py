from flask import jsonify, Blueprint
from role_skill.roleSkillService import RoleSkillService
role_skill_bp = Blueprint('role_skill', __name__)

# Get role skills by role_name
@role_skill_bp.route('/get_skills_by_role_name/<role_name>')
def get_skills_by_role_name(role_name):
    try:
        response = RoleSkillService.get_skill_by_role_name(role_name)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@role_skill_bp.route('/get_skills')
def get_all_skills():

    RoleSkillService.importRoleSkill()
    response = RoleSkillService.get_all_skills()
    return response, 200

