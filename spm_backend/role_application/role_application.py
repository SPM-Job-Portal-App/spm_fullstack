from flask import jsonify, request, Blueprint
from models import db, RoleApplication
from role_listings.listingService import Listing
from datetime import datetime

application_bp = Blueprint('application', __name__)

@application_bp.route('/', methods=['GET'])
def test():
    return "It works!"

# apply for role listing
@application_bp.route('/', methods=['POST'])
def apply_for_role_listing():
    data = request.get_json()
    listing_data = Listing.get_listing_by_index(data['role_listing'])
    if not listing_data:
        return jsonify({'message': 'Application at index does not exist'}), 200
    else:
        is_open = listing_data['is_open']
        if not is_open:
            return jsonify({'message': 'Application is closed'}), 200
        else:
            current_datetime = datetime.now()
            formatted_date = current_datetime.strftime("%Y-%m-%d")
            new_application = RoleApplication(
                application_date=formatted_date,
                role_listing_id=data['role_listing'],
                staff_id=data['staff_id']
            )
            db.session.add(new_application)
            db.session.commit()
            return jsonify({'message': 'Role application created successfully'}), 201
    