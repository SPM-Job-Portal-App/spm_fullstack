from models.staff_model import Staff
from models.model import db
import csv
from flask import jsonify, request, Blueprint

class StaffService():
    # get a staff by staff id
    def get_staff_by_id(staff_id):
        
        try:
            staff_response = Staff.query.filter(Staff.id == staff_id).first()

            # if staff is None, that is no staff found, raise an exception
            if not staff_response:
                raise Exception("No staff with this id found")
                    
            # if staff is found
            staff = {
                'staff_first_name': staff_response.staff_first_name,
                'staff_last_name': staff_response.staff_last_name,
                'dept': staff_response.dept,
                'country': staff_response.country,
                'email': staff_response.email,
                'role': staff_response.role  
            }

            return staff
        
        except Exception as e:
            raise Exception("No staff with this id found")
        
    # get all staff
    def get_all_staff():
    
            try:
                staff_response = Staff.query.all()
    
                if len(staff_response):
                    return jsonify(
                        {
                            "code": 200,
                            "staff": [staff.json() for staff in staff_response]
                        }
                    )
                return jsonify(
                    {
                        "code": 404,
                        "message": "There are no staff."
                    }
                ), 404
        
            except Exception as e:
                raise Exception("No staff found")
        

    def importRoleSkill():
        existing_role_count = db.session.query(Staff).count()
    
        if existing_role_count > 0:
            return 
        with open('./staff/staff.csv', newline='',encoding='utf-8-sig',errors='replace') as csv_file:
            csvreader = csv.DictReader(csv_file)
            
            for row in csvreader:
               
              
                new_staff = Staff(
                    id=row['Staff_ID'],
                    staff_first_name=row['Staff_FName'],
                    staff_last_name=row['Staff_LName'],
                    dept = row['Dept'],
                    country = row['Country'],
                    email=row['Email'],
                    role=row['Role']





                    
                )
                db.session.add(new_staff)
            db.session.commit()
            
        return jsonify({'message': 'Roles Updated'}), 201
    

            