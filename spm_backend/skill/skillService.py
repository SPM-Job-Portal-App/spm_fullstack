from models.skill_model import Skill
import csv
from models.model import db
from flask import jsonify;

class SkillService():
    def get_all_skills():

        try:
            skills_response = Skill.query.all()

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
        
        
    def import_skills():
        with open('./skill/skill.csv', newline='',encoding='utf-8-sig',errors='replace') as csv_file:
            csvreader = csv.DictReader(csv_file)
            
            for row in csvreader:
               
                new_skill = Skill(
                    skill_name=row['Skill_Name'],
                    skill_description=row['Skill_Desc'],
                    
                )
                db.session.add(new_skill)
            db.session.commit()
            
        return jsonify({'message': 'Roles Updated'}), 201



# class SkillService():
#     def get_skills_by_role_name():
#         return "Hello"