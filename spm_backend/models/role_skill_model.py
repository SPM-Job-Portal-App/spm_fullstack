from models.model import db
from sqlalchemy.dialects.mysql import LONGTEXT

class RoleSkill(db.Model):
    role_name = db.Column(db.String(50), db.ForeignKey('role.role_name'), primary_key=True)
    skill_name = db.Column(db.String(50), db.ForeignKey('skill.skill_name'), primary_key=True)

    def __init__(self, role_name, skill_name):
        self.role_name = role_name
        self.skill_name = skill_name

