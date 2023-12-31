from models.role_listing_model import RoleListing
from models.staff_model import Staff
from models.model import db
from staff.staffService import StaffService
from role.roleService import RoleService
from role_skill.roleSkillService import RoleSkillService
from flask import jsonify

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


    # get all listings, open and closed
    def get_all_listing():
        listings = RoleListing.query.all()

        if len(listings) == 0:
            raise Exception('No role listings')
        
        # if got listings
        role_listing_list = []
        for listing in listings:
            
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
                'opening_date': listing.opening_date,
                'closing_date': listing.closing_date,
                'reporting_manager': reporting_manager_full_name,
                'description': description
            }
            role_listing_list.append(listing_data)
        
        return role_listing_list

    
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
                'opening_date': listing.opening_date,
                'closing_date': listing.closing_date,
                'reporting_manager': reporting_manager_full_name,
                'description': description
            }
            open_listing_list.append(listing_data)
        
        return open_listing_list

    
    #  view specific open role listing by id
    def get_listing_by_index(id):
        listing = RoleListing.query.get(id)
        if listing is None:
            return jsonify({"message": f"Listing at index {id} does not exist"}), 404
        listing_data = {
            'id': listing.id,
            'role_name': listing.role_name,
            # 'skills': listing.skills,
            'country': listing.country,
            'dept': listing.dept,
            'is_open': listing.is_open,
            'opening_date': listing.opening_date,
            'closing_date': listing.closing_date,
            'reporting_manager': listing.reporting_manager
        }
        return listing_data, 201
    
    # create role listing addition
    def create_role_listing_feature(data):
        # Extract data from the input
        role_name = data.get('role_name')
        # skills = data.get('skills')
        country = data.get('country')
        dept = data.get('dept')
        is_open = data.get('is_open')
        opening_date = data.get('opening_date')
        closing_date = data.get('closing_date')
        reporting_manager = data.get('reporting_manager')
        
        # Validate the incoming data (e.g., check for required fields)
        # if not role_name or not skills or not country or not dept:
        if not role_name or not country or not dept or not opening_date:
            return {"message": "Missing required fields"}, 400

        # Check if a role listing with the same attributes exists
        existing_listing = RoleListing.query.filter_by(
            role_name=role_name,
            # skills=skills,
            country=country,
            dept=dept,
            is_open=is_open,
            opening_date=opening_date,
            closing_date=closing_date,
            reporting_manager=reporting_manager
        ).first()

        if existing_listing:
            return jsonify({"message": "Role Listing already exists"}), 409  # Conflict
        # check if staff exists
        staff = Staff.query.get(reporting_manager)
        if reporting_manager and not staff:
            return jsonify({"message": "Reporting manager does not exist"}), 404
         
        # Create a new RoleListing object
        new_role = RoleListing(
            role_name=role_name,
            # skills=skills,
            country=country,
            dept=dept,
            is_open=is_open,
            opening_date=opening_date,
            closing_date=closing_date,
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
    
    # edit role listing information
    def edit_role_listing(id, data):
        role_name = data.get('role_name')
        # skills = data.get('skills')
        country = data.get('country')
        dept = data.get('dept')
        is_open = data.get('is_open')
        opening_date = data.get('opening_date')
        closing_date = data.get('closing_date')
        reporting_manager = data.get('reporting_manager')

        # if role listing information is missing
        # if not role_name or not skills or not country or not dept or not opening_date or not closing_date:
        if not role_name or not country or not dept or not opening_date or not closing_date:
            return jsonify({"message": "Missing required fields"}), 400
        
        # if role listing at id does not exist
        existing_listing = RoleListing.query.get(id)
        if not existing_listing:
            return jsonify({'message': "Role listing at index does not exist"}), 404
        
        # if role listing is closed
        existing_listing_is_open = existing_listing.is_open
        if not existing_listing_is_open:
            return jsonify({'message': "Role listing at index is already closed"}), 400
        
        existing_listing.role_name = role_name
        # existing_listing.skills = skills
        existing_listing.country = country
        existing_listing.dept = dept
        existing_listing.is_open = is_open
        existing_listing.opening_date = opening_date
        existing_listing.closing_date = closing_date
        existing_listing.reporting_manager = reporting_manager
        db.session.commit()
        return jsonify({'message': 'Role listing updated successfully'}), 201
        
    # update role listing
    def update_role_listing(id, data):
        # Get the existing role listing by its ID
        existing_listing = RoleListing.query.get(id)

        if existing_listing is None:
            return {"message": "Role Listing not found"}, 404  # Not Found

        # Extract data from the input (only update fields that are provided)
        role_name = data.get('role_name', existing_listing.role_name)
        skills = data.get('skills', existing_listing.skills)
        country = data.get('country', existing_listing.country)
        dept = data.get('dept', existing_listing.dept)
        is_open = data.get('is_open', existing_listing.is_open)
        reporting_manager = data.get('reporting_manager', existing_listing.reporting_manager)

        # Update the existing role listing with the new data
        existing_listing.role_name = role_name
        existing_listing.skills = skills
        existing_listing.country = country
        existing_listing.dept = dept
        existing_listing.is_open = is_open
        existing_listing.reporting_manager = reporting_manager

        try:
            db.session.commit()
            return {"message": "Role Listing updated successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while updating the Role Listing"}, 500
        
    # close role listing
    def close_role_listing(id):
        # get the role listing by id
        # update the field is_open from true to false

        listing = db.session.query(RoleListing).filter(RoleListing.id == id).first()
        
        # if listing is None
        if not listing:
            raise Exception(f"Listing with id {id} not found so cannot close it!")
        
        # check whether role listing is already closed. If already closed then raise Exception
        if not listing.is_open:
            raise Exception(f"Listing with id {id} already closed and so cannot be closed again!")
        
        # if not, can update to close
        try:
            db.session.query(RoleListing).filter(RoleListing.id == id).update({'is_open': False})
            db.session.commit()
            return {'message': f"Role listing with id {id} closed successfully"}, 200
        except Exception as e:
            return {'message': f"An error occurred while closing role listing with id {id}"}, 500
            
