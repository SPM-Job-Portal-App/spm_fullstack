from models.model import db
from models.role_application_model import RoleApplication
from role_listings.listingService import Listing
from datetime import datetime
from flask import jsonify

class Application():
    def apply_for_role(data):
        listing_data, listing_data_status = Listing.get_listing_by_index(data['role_listing'])
        # if listing does not exist
        if listing_data_status == 404:
            return jsonify({'message': 'Role listing at index does not exist'}), 404
        
        # if listing is not open
        is_open = listing_data['is_open']
        if not is_open:
            return jsonify({'message': 'Application is closed'}), 400
        
        # if staff has already applied for listing
        existing_application = db.session.query(RoleApplication).filter_by(
            staff_id=data['staff_id'],
            role_listing_id=data['role_listing']
        ).first()
        if existing_application:
            return jsonify({'message': 'You have already applied for this role listing'}), 400
        
        # if staff has not applied for listing
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime("%y-%m-%d")
        new_application = RoleApplication(
            application_date=formatted_date,
            role_listing_id=data['role_listing'],
            staff_id=data['staff_id']
        )
        db.session.add(new_application)
        db.session.commit()
        return jsonify({'message': 'Role application created successfully'}), 201