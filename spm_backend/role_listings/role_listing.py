from flask_sqlalchemy import SQLAlchemy

from models import db

class RoleListing(db.Model):
    
    role_name = db.Column(db.String(255), primary_key=True)
    skills = db.Column(db.String(255), primary_key=True)
    country = db.Column(db.String(255),nullable=True)
    dept = db.Column(db.String(255),nullable=True)
    is_open = db.Column(db.Boolean,nullable=True)
    reporting_manager = db.Column(db.Integer, db.ForeignKey('staff.id'),nullable=True)

    def __init__(self, role_name, skills, country=None, dept=None, is_open=None, reporting_manager=None):
        self.role_name = role_name
        self.skills = skills
        self.country = country
        self.dept = dept
        self.is_open = is_open
        self.reporting_manager = reporting_manager