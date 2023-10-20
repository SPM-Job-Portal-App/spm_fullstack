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
    
    def get_role_applications():
        listings = Listing.get_all_open_listing()
        applications = RoleApplication.query.all()
        application_list = []
        for application in applications:
            application_data = {
                'id': application.id,
                'application_date': application.application_date,
                'role_listing_id': application.role_listing_id,
                'staff_id': application.staff_id,
            }
            application_list.append(application_data)
        combined_list = []
        for listing in listings:
            applicants = []
            for application in application_list:
                if application['role_listing_id'] == listing['id']:
                    applicants.append({'id': application['id'], 'application_date': application['application_date'], 'staff_id': application['staff_id']})
            combined_data = {
                'id': listing['id'],
                'role_name': listing['role_name'],
                'skills': listing['skills'],
                'country': listing['country'],
                'dept': listing['dept'],
                'is_open': listing['is_open'],
                'reporting_manager': listing['reporting_manager'],
                'applicants': applicants
            }
            combined_list.append(combined_data)
        return combined_list
    
    def get_role_application_by_listing_id(role_listing_id):
        try:
            role_application_response = RoleApplication.query.filter(RoleApplication.role_listing_id == role_listing_id).all()
            if not role_application_response:
                raise Exception("No application found for role listing with ID: " + str(role_listing_id))
            applicants_list = [role_application.staff_id for role_application in role_application_response]
            return applicants_list
        except Exception as e:
            raise Exception("No applicants found")