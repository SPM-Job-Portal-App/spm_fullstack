from models.model import db

class RoleListing(db.Model):
    # __tablename__ = 'rolelisting'
    id = db.Column(db.Integer, primary_key=True)
    # role_name = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    dept = db.Column(db.String(255), nullable=False)
    is_open = db.Column(db.Boolean, nullable=False)
    opening_date = db.Column(db.Date, nullable=False)
    closing_date = db.Column(db.Date, nullable=False)
    # reporting_manager = db.Column(db.Integer, nullable=True)
    
    # Define foreign key
    role_name = db.Column(db.String(255), db.ForeignKey('role.role_name'), nullable=False)
    reporting_manager = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=True)
    
    # relationships
    # var = db.relationship('Role', foreign_keys=[role_name], cascade="save-update, merge")
    # var2 = db.relationship('Role', foreign_keys=[reporting_manager], cascade="save-update, merge")

    def __init__(self, role_name, country, dept, is_open, opening_date, closing_date, reporting_manager):
        self.role_name = role_name
        self.country = country
        self.dept = dept
        self.is_open = is_open
        self.opening_date = opening_date
        self.closing_date = closing_date
        self.reporting_manager = reporting_manager
