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
    
# get listing data by id
@listing_bp.route('/<int:id>', methods=['GET'])
def get_role_listing_data_by_id(id):
    try:
        response, status_code = Listing.get_listing_by_index(id)
        return response, status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# edit role listing data by id
@listing_bp.route('/<int:id>', methods=['PUT'])
def edit_role_listing_data_by_id(id):
    data = request.get_json()
    try:
        response, status_code = Listing.edit_role_listing(id, data)
        return response, status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500