from models.skill_model import Skill
import csv
from models.model import db
from flask import jsonify;

class SkillService():
    def get_skill_by_skill_name(skill_name_input):
        try:
            skills_response = Skill.query.filter(Skill.skill_name == skill_name_input).first()

            skill = {
                'skill_name': skills_response.skill_name,
                'skill_desc': skills_response.skill_description
            }

            return skill
        
        except Exception as e:
            raise Exception("No skill with the skill_name found")

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
        existing_skill_count = db.session.query(Skill).count()
    
        if existing_skill_count > 0:
            return 
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