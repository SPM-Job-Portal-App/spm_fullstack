
from models.model import db

class Skill(db.Model):
    skill_name = db.Column(db.String(255), nullable=False,primary_key=True)
    skill_description = db.Column(db.Text, nullable=False)
   
    

    def __init__(self, skill_name,skill_description):
        self.skill_name = skill_name
        self.skill_description = skill_description
       
    def json(self):
        return {"Skill Name": self.skill_name, "Skill Description": self.skill_description}
    
