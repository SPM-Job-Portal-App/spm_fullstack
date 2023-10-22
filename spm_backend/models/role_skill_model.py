from models.model import db;
class RoleSkill(db.Model):
    
    # Define the foreign keys
    role_name = db.Column(db.String(50), db.ForeignKey('role.role_name'), primary_key =True ,nullable=False)
    skill_name = db.Column(db.String(50), db.ForeignKey('skill.skill_name'), primary_key = True,nullable=False)

    # Define the relationships
    role = db.relationship('Role', backref='role_skills', foreign_keys=[role_name])
    skill = db.relationship('Skill', backref='skill_roles', foreign_keys=[skill_name])

    def __init__(self, role_name, skill_name):
        self.role_name = role_name
        self.skill_name = skill_name
    def json(self):
        return {"Role Name": self.role_name, "Skill Name": self.skill_name}

