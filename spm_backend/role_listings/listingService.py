from models import db, RoleListing

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
                'reporting_manager': listing.reporting_manager
            }
            listing_list.append(listing_data)
        return listing_list
    
    def get_listing_by_index(id):
        listing = db.session.get(RoleListing, id)
        if listing is None:
            return None
        listing_data = {
            'id': listing.id,
            'role_name': listing.role_name,
            'skills': listing.skills,
            'country': listing.country,
            'dept': listing.dept,
            'is_open': listing.is_open,
            'reporting_manager': listing.reporting_manager
        }
        return listing_data