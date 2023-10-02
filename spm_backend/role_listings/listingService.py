from models.role_listing_model import RoleListing
from models.model import db
from flask import jsonify

class Listing():
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