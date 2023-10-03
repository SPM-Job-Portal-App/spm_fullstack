from models.role_listing_model import RoleListing
from models.model import db
from staff.staffService import StaffService
from role.roleService import RoleService
from role_skill.roleSkillService import RoleSkillService

class Listing():
    # helper functions
    # to get staff using staff id
    def get_staff_full_name_with_id(id):
        try:
            staff_response = StaffService.get_staff_by_id(id)
            return staff_response['staff_first_name'] + " " + staff_response['staff_last_name']
        except Exception as e:
            return "Nil"

    # to get role description using role_name
    def get_role_desc(role_name):
        try:
            role_response = RoleService.get_role_by_role_name(role_name)
            return role_response['role_desc']
        except Exception as e:
            return "Nil"
        
    # to get skills for a role using role_name
    def get_skills_with_role_name(role_name):
        try:
            skills_response = RoleSkillService.get_skills_by_role_name(role_name)
            return skills_response
        except Exception as e:
            return []


    def get_all_listing():
        listings = RoleListing.query.all()
        listing_list = []
        for listing in listings:
            listing_data = {
                'id': listing.id,
                'role_name': listing.role_name,
                'skills': listing.skills,
                'country': listing.country,
                'dept': listing.dept,
                'is_open': listing.is_open,
                'reporting_manager': listing.reporting_manager
            }
            listing_list.append(listing_data)
        return listing_list
    
    # get all open roles
    def get_all_open_listing():
        open_listings = RoleListing.query.filter(RoleListing.is_open == True).all()

        # no open listings
        if len(open_listings) == 0:
            raise Exception('No open role listings')
        
        # if got open listings
        open_listing_list = []
        for listing in open_listings:
            
            # get reporting_manager using staff id
            reporting_manager_full_name = Listing.get_staff_full_name_with_id(listing.reporting_manager)
            # get role description using role_name 
            description = Listing.get_role_desc(listing.role_name)
            # get skills for a role using role_name
            skills_list = Listing.get_skills_with_role_name(listing.role_name)
            skills_string = "Nil"
            
            # if skills list is not empty then only update skills_string
            if skills_list != []:
                skills_string = ", ".join(skills_list)

            listing_data = {
                'id': listing.id,
                'role_name': listing.role_name,
                'skills': skills_string,
                'country': listing.country,
                'dept': listing.dept,
                'is_open': listing.is_open,
                'reporting_manager': reporting_manager_full_name,
                'description': description
            }
            open_listing_list.append(listing_data)
        
        return open_listing_list

    
    def get_listing_by_index(id):
        listing = RoleListing.query.get(id)
        if listing is None:
            return None
        listing_data = {
            'id': listing.id,
            'role_name': listing.role_name,
            'skills': listing.skills,
            'country': listing.country,
            'dept': listing.dept,
            'is_open': listing.is_open,
            'reporting_manager': listing.reporting_manager
        }
        return listing_data
    
    # create role listing addition
    def create_role_listing_feature(data):
        # Extract data from the input
        role_name = data.get('role_name')
        skills = data.get('skills')
        country = data.get('country')
        dept = data.get('dept')
        is_open = data.get('is_open')
        reporting_manager = data.get('reporting_manager')
        
        # Validate the incoming data (e.g., check for required fields)
        if not role_name or not skills or not country or not dept:
            return {"message": "Missing required fields"}, 400

        # Check if a role listing with the same attributes exists
        existing_listing = RoleListing.query.filter_by(
            role_name=role_name,
            skills=skills,
            country=country,
            dept=dept,
            is_open=is_open,
            reporting_manager=reporting_manager
        ).first()

        if existing_listing:
            return {"message": "Role Listing already exists"}, 409  # Conflict

        # Create a new RoleListing object
        new_role = RoleListing(
            role_name=role_name,
            skills=skills,
            country=country,
            dept=dept,
            is_open=is_open,
            reporting_manager=reporting_manager
        )

        # Add the new role to the database
        db.session.add(new_role)

        try:
            db.session.commit()
            return {"message": "Role Listing created successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while creating the Role Listing"}, 500