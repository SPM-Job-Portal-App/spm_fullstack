from models.model import db

class Role(db.Model):
    role_name = db.Column(db.String(255), nullable=False,primary_key=True)
    skill_name = db.Column(db.String(255), nullable=False,primary_key=True)
    description = db.Column(db.String(255))
    department = db.Column(db.String(255))
    

    def __init__(self, role_name,skill_name,description,department):
        self.role_name = role_name
        self.skill_name = skill_name
        self.description = description
        self.department = department
    def json(self):
        return {"label": self.role_name, "skill": self.skill_name, "description": self.description,"department":self.department}
    
    

        