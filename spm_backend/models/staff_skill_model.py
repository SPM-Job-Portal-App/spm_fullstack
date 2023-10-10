
from models.model import db

class StaffSkill(db.Model):
    __tablename__ = 'staff_skill'
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), primary_key=True, nullable=False)
    skill_name = db.Column(db.String(50), db.ForeignKey('skill.skill_name'), primary_key=True, nullable=False)

    # Define the relationships (optional)
    staff = db.relationship("Staff", back_populates="skills")
    skill = db.relationship("Skill", back_populates="staff")


    def __init__(self, staff_id, skill_name):
        self.staff_id = staff_id
        self.skill_name = skill_name

    def json(self):
        return {"Staff Id": self.staff_id, "Skill Name ": self.skill_name}
    