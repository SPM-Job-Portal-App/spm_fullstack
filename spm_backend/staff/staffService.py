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
    
    # Get all staff members
    def get_all_staff():
        # Use SQLAlchemy to query the database to retrieve all staff members
        staff_list = Staff.query.all()

        # Convert the list of staff objects into a list of dictionaries
        staff_info_list = []
        for staff_response in staff_list:
            staff_info = {
                'staff_id': staff_response.id,
                'staff_first_name': staff_response.staff_first_name,
                'staff_last_name': staff_response.staff_last_name,
                'dept': staff_response.dept,
                'country': staff_response.country,
                'email': staff_response.email,
                'role': staff_response.role  
            }
            staff_info_list.append(staff_info)

        # Return the list of staff information as a list of dictionaries
        return staff_info_list       