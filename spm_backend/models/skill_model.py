from models.model import db

class Skill(db.Model):
    __tablename__ = 'skill'
    skill_name = db.Column(db.String(255), nullable=False,primary_key=True)
    skill_desc = db.Column(db.Text, nullable=False)
    staff = db.relationship("StaffSkill", back_populates="skill")
   
    def __init__(self, skill_name,skill_desc):
        self.skill_name = skill_name
        self.skill_desc = skill_desc
       
    def json(self):
        return {"Skill Name": self.skill_name, "Skill Description": self.skill_desc}
    
