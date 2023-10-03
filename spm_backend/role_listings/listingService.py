from models.role_listing_model import RoleListing
from models.staff_model import Staff
from models.model import db
from flask import jsonify
import re

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
                'opening_date': listing.opening_date,
                'closing_date': listing.closing_date,
                'reporting_manager': listing.reporting_manager
            }
            listing_list.append(listing_data)
        return listing_list
    
    #  view specific open role listing by id
    def get_listing_by_index(id):
        listing = RoleListing.query.get(id)
        if listing is None:
            return jsonify({"message": f"Listing at index {id} does not exist"}), 404
        listing_data = {
            'id': listing.id,
            'role_name': listing.role_name,
            'skills': listing.skills,
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
        skills = data.get('skills')
        country = data.get('country')
        dept = data.get('dept')
        is_open = data.get('is_open')
        opening_date = data.get('opening_date')
        closing_date = data.get('closing_date')
        reporting_manager = data.get('reporting_manager')
        
        # Validate the incoming data (e.g., check for required fields)
        if not role_name or not skills or not country or not dept or not opening_date or not closing_date:
            return jsonify({"message": "Missing required fields"}), 400

        # Check if a role listing with the same attributes exists
        existing_listing = RoleListing.query.filter_by(
            role_name=role_name,
            skills=skills,
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
            skills=skills,
            country=country,
            dept=dept,
            is_open=is_open,
            opening_date=opening_date,
            closing_date=closing_date,
            reporting_manager=reporting_manager
        )
        # Add the new role to the database
        db.session.add(new_role)
        db.session.commit()
        return jsonify({"message": "Role Listing created successfully"}), 201
    
    # edit role listing information
    def edit_role_listing(id, data):
        role_name = data.get('role_name')
        skills = data.get('skills')
        country = data.get('country')
        dept = data.get('dept')
        is_open = data.get('is_open')
        opening_date = data.get('opening_date')
        closing_date = data.get('closing_date')
        reporting_manager = data.get('reporting_manager')

        # if role listing information is missing
        if not role_name or not skills or not country or not dept or not opening_date or not closing_date:
            return jsonify({"message": "Missing required fields"}), 400
        
        # if role listing at id does not exist
        existing_listing = RoleListing.query.get(id)
        if not existing_listing:
            return jsonify({'message': "Role listing at index does not exist"}), 404
        
        # if role listing is closed
        existing_listing_is_open = existing_listing.is_open
        if not existing_listing_is_open:
            return jsonify({'message': "Role listing at index is already closed"}), 400
        
        # if opening date and closing date in wrong format
        date_pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(date_pattern, opening_date) or not re.match(date_pattern, closing_date):
            return jsonify({'message': "Opening and closing date inputs must be in YYYY-MM-DD format"}), 400
        existing_listing.role_name = role_name
        existing_listing.skills = skills
        existing_listing.country = country
        existing_listing.dept = dept
        existing_listing.is_open = is_open
        existing_listing.opening_date = opening_date
        existing_listing.closing_date = closing_date
        existing_listing.reporting_manager = reporting_manager
        db.session.commit()
        return jsonify({'message': 'Role listing updated successfully'}), 201