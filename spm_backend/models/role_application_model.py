from models.model import db

class RoleApplication(db.Model):
    __tablename__ = 'role_application'

    id = db.Column(db.Integer, primary_key=True)
    application_date = db.Column(db.Date, nullable=False)
    role_listing_id = db.Column(db.Integer, nullable=False)
    staff_id = db.Column(db.Integer, nullable=False)

    def __init__(self, application_date, role_listing_id, staff_id):
        self.application_date = application_date
        self.role_listing_id = role_listing_id
        self.staff_id = staff_id