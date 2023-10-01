from flask import jsonify, request, Blueprint
from role_listings.listingService import Listing
listing_bp = Blueprint('listing', __name__)

# Create New Role Listing
@listing_bp.route('/create', methods=['POST'])
def create_role_listing():
    data = request.get_json()
    try:
        response, status_code = Listing.create_role_listing_feature(data)
        return response, status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500