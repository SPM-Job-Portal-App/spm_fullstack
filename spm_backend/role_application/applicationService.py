from models.model import db
from models.role_application_model import RoleApplication
from role_listings.listingService import Listing
from datetime import datetime
from flask import jsonify

class Application():
    def apply_for_role(data):
        listing_data = Listing.get_listing_by_index(data['role_listing'])
        # if listing does not exist
        if not listing_data:
            return jsonify({'message': 'Role listing at index does not exist'}), 404
        # if listing exists
        else:
            is_open = listing_data['is_open']
            # if listing is not open
            if not is_open:
                return jsonify({'message': 'Application is closed'}), 400
            # if listing is open
            else:
                # if staff has already applied for listing
                existing_application = db.session.query(RoleApplication).filter_by(
                    staff_id=data['staff_id'],
                    role_listing_id=data['role_listing']
                ).first()
                if existing_application:
                    return jsonify({'message': 'You have already applied for this role listing'}), 400
                else:
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

    def get_role_listing_by_staff_id_application(id):
        applications = db.session.query(RoleApplication).filter_by(staff_id=id).all()
        applied_role_listings = []
        for application in applications:
            role_listing = Listing.get_listing_by_index(application.role_listing_id)
            applied_role_listings.append(role_listing)
        return jsonify({
            'message': 'Applied role listings by staff id retrieved successfully',
            'applied_role_listings': applied_role_listings
        }), 201