from models.model import db
from sqlalchemy.dialects.mysql import LONGTEXT

class RoleSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), nullable=False)
    skill_name = db.Column(db.String(50), nullable=False)

    def __init__(self, role_name, skill_name):
        self.role_name = role_name
        self.skill_name = skill_name

