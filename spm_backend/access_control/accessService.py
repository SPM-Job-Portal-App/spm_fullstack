from models.access_contol_model import AccessControl
import csv
from models.model import db
from flask import jsonify;

class AccessService():
   

    def get_all_access():

        try:
            access_response = AccessControl.query.all()

            if len(access_response):
                return jsonify(
                    {
                        "code": 200,
                        "Access": [access.json() for access in access_response]
                    }
                )
            return jsonify(
                {
                    "code": 404,
                    "message": "There are no access."
                }
            ), 404
      
        except Exception as e:
            raise Exception("No skills found")
        
        
    def import_access():
        existing_skill_count = db.session.query(AccessControl).count()
    
        if existing_skill_count > 0:
            return 
        with open('./access_control/access_control.csv', newline='',encoding='utf-8-sig',errors='replace') as csv_file:
            csvreader = csv.DictReader(csv_file)
            
            for row in csvreader:
               
                access = AccessControl(
                    access_id=row['Access_ID'],
                    access_control_name=row['Access_Control_Name'],
                    
                )
                db.session.add(access)
            db.session.commit()
            
        return jsonify({'message': 'access Updated'}), 201