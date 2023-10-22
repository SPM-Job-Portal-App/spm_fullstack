from models.role_skill_model import RoleSkill
from models.model import db;
import csv;
from flask import jsonify;

class RoleSkillService():
    def get_skills_by_role_name(role_name_input):
        try:
            role_skills_response = RoleSkill.query.filter(RoleSkill.role_name == role_name_input).all()

            skills_list = []
            for role_skill in role_skills_response:
                skills_list.append(role_skill.skill_name)

            if len(skills_list) == 0:
                raise Exception("No skills with this role name found")

            return skills_list
        except Exception as e:
                raise Exception("No skills with this role name found")

    def get_all_skills():

        try:
            skills_response = RoleSkill.query.all()

            if len(skills_response):
                return jsonify(
                    {
                        "code": 200,
                        "skills": [skill.json() for skill in skills_response]
                    }
                )
            return jsonify(
                {
                    "code": 404,
                    "message": "There are no crops."
                }
            ), 404
      
        except Exception as e:
            raise Exception("No skills found")
        
    def importRoleSkill():
        existing_role_count = db.session.query(RoleSkill).count()
    
        if existing_role_count > 0:
            return 
        with open('./role_skill/role_skill.csv', newline='',encoding='utf-8-sig',errors='replace') as csv_file:
            csvreader = csv.DictReader(csv_file)
            
            for row in csvreader:
               
              
                new_role_skill = RoleSkill(
                    role_name=row['Role_Name'],
                    skill_name=row['Skill_Name'],
                    
                )
                db.session.add(new_role_skill)
            db.session.commit()
            
        return jsonify({'message': 'Roles Updated'}), 201

