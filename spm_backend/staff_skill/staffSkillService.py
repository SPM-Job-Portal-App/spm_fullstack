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
    
    def get_staff_skills(id):
        try:
            staff_skills_response = StaffSkill.query.filter(StaffSkill.staff_id == id)
            if not staff_skills_response:
                raise Exception("No skills found for staff with ID: " + str(id))
            skills_list = [skill.skill_name for skill in staff_skills_response]
            return skills_list
            # for skill in staff_skills_response:
            #     skills_list.append(skill.skill_name)
        except Exception as e:
            raise Exception("No skills found")