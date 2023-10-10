from models.staff_skill_model import StaffSkill
import csv
from models.model import db
from flask import jsonify;
class StaffSkillService():
    def get_all_skills():

            try:
                skills_response = StaffSkill.query.all()

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
        existing_skill_count = db.session.query(StaffSkill).count()

        if existing_skill_count > 0:
            return 
        with open('./staff_skill/staff_skill.csv', newline='',encoding='utf-8-sig',errors='replace') as csv_file:
            csvreader = csv.DictReader(csv_file)
            
            for row in csvreader:
                
                staff_skill = StaffSkill(
                    staff_id=row['Staff_ID'],
                    skill_name =row['Skill_Name'],
                    
                )
                db.session.add(staff_skill)
            db.session.commit()
            
        return jsonify({'message': 'Roles Updated'}), 201