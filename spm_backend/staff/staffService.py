from models.staff_model import Staff
from models.model import db

class StaffService():
    # get a staff by staff id
    def get_staff_by_id(staff_id):
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

            