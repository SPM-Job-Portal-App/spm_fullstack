from models.model import db
from models.staff_model import Staff

class RoleListing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(255), nullable=False)
    # skills = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    dept = db.Column(db.String(255), nullable=False)
    is_open = db.Column(db.Boolean, nullable=False)
    opening_date = db.Column(db.Date, nullable=False)
    closing_date = db.Column(db.Date, nullable=False)
    reporting_manager = db.Column(db.Integer, db.ForeignKey('staff.id'))


    def __init__(self, role_name, country, dept, is_open, reporting_manager):
        self.role_name = role_name
        self.country = country
        self.dept = dept
        self.is_open = is_open
        self.opening_date = opening_date
        self.closing_date = closing_date
        self.reporting_manager = reporting_manager
