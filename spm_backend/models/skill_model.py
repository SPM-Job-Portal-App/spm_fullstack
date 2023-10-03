from models.model import db
from sqlalchemy.dialects.mysql import LONGTEXT

class Skill(db.Model):
    skill_name = db.Column(db.String(50), primary_key=True)
    skill_desc = db.Column(LONGTEXT)

    def __init__(self, skill_name, skill_desc):
        self.skill_name = skill_name
        self.skill_desc = skill_desc

