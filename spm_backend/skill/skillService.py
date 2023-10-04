from models.skill_model import Skill

class SkillService():
    def get_skills_by_role_name():

        try:
            skills_response = Skill.query.all()

            skills_list = []
            for skill in skills_response:
                skills_list.append(skill.skill_name)

            return skills_list

        except Exception as e:
            raise Exception("No skills found")

# class SkillService():
#     def get_skills_by_role_name():
#         return "Hello"