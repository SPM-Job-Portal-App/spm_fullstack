from flask import jsonify, request, Blueprint
from models import db, RoleListing
from role_listings.listingService import Listing

listing_bp = Blueprint('listing', __name__)

@listing_bp.route('/', methods=['POST'])
def create_role_listing():
    data = request.get_json()
    new_listing = RoleListing(
        role_name=data['role_name'],
        skills=data['skills'],
        country=data['country'],
        dept=data['dept'],
        is_open=data['is_open'],
        reporting_manager=data.get('reporting_manager')
    )
    db.session.add(new_listing)
    db.session.commit()
    return jsonify({'message': 'Role listing created successfully'}), 201

# Read all role listings
@listing_bp.route('/', methods=['GET'])
def get_all_role_listings():
    return jsonify(Listing.get_all_listing(), 200)

# Read a specific role listing by ID
@listing_bp.route('/<int:id>', methods=['GET'])
def get_role_listing(id):
    res = Listing.get_listing_by_index(id)
    if not res:
        return jsonify({'message': 'Role listing not found'}), 404
    return jsonify(res), 200

# Update
@listing_bp.route('/<int:id>', methods=['PUT'])
def update_role_listing(id):
    listing = RoleListing.query.get(id)
    if listing is None:
        return jsonify({'message': 'Role listing not found'}), 404
    data = request.get_json()
    listing.role_name = data['role_name']
    listing.skills = data['skills']
    listing.country = data['country']
    listing.dept = data['dept']
    listing.is_open = data['is_open']
    listing.reporting_manager = data.get('reporting_manager')
    db.session.commit()
    return jsonify({'message': 'Role listing updated successfully'}), 200

# Delete
@listing_bp.route('/<int:id>', methods=['DELETE'])
def delete_role_listing(id):
    listing = RoleListing.query.get(id)
    if listing is None:
        return jsonify({'message': 'Role listing not found'}), 404
    db.session.delete(listing)
    db.session.commit()
    return jsonify({'message': 'Role listing deleted successfully'}), 200