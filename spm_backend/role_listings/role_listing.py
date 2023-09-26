from flask import jsonify, request, Blueprint
from models import db, RoleListing
from role_listings.listingService import Listing

listing_bp = Blueprint('listing', __name__)

# @listing_bp.route('/', methods=['POST'])
# def create_role_listing():
#     data = request.get_json()
#     new_listing = RoleListing(
#         role_name=data['role_name'],
#         skills=data['skills'],
#         country=data['country'],
#         dept=data['dept'],
#         is_open=data['is_open'],
#         reporting_manager=data.get('reporting_manager')
#     )
#     db.session.add(new_listing)
#     db.session.commit()
#     return jsonify({'message': 'Role listing created successfully'}), 201

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



######################### Create Role Listing #########################
@listing_bp.route('/create', methods=['POST'])
def create_role_listing():
    data = request.get_json()
    
    # role_listing_id = data['role_listing_id']
    role_name = data['role_name']
    skills = data['skills']
    country = data['country']
    dept = data['dept']
    is_open = data['is_open']
    reporting_manager = data['reporting_manager']
    
    # Validate the incoming data (e.g., check for required fields)
    if not role_name or not skills or not country or not dept:
        return jsonify({"message": "Missing required fields"}), 400

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
        return jsonify({"message": "Role Listing already exists"}), 409  # Conflict

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
        return jsonify({"message": "Role Listing created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "An error occurred while creating the Role Listing"}), 500
    