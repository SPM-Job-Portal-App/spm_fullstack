from flask import jsonify, request, Blueprint
from role_listings.listingService import Listing
listing_bp = Blueprint('listing', __name__)

# Get all Open Role Listings
@listing_bp.route('/get_open_listings')
def get_all_open_listing():
    try:
        response = Listing.get_all_open_listing()
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create New Role Listing
@listing_bp.route('/create', methods=['POST'])
def create_role_listing():
    data = request.get_json()
    try:
        response, status_code = Listing.create_role_listing_feature(data)
        return response, status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500