from models.role_skill_model import RoleSkill

class RoleSkillService():
    def get_skills_by_role_name(role_name_input):

        try:
            role_skills_response = RoleSkill.query.filter(RoleSkill.role_name == role_name_input).all()

            skills_list = []
            for role_skill in role_skills_response:
                skills_list.append(role_skill.skill_name)

            return skills_list

        except Exception as e:
            raise Exception("No skills with this role name found")

