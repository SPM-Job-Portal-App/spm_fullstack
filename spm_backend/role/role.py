from models import db
class Role(db.Model):
    role_name = db.Column(db.String(255), nullable=False,primary_key=True)
    skill_name = db.Column(db.String(255), nullable=False,primary_key=True)
    

    def __init__(self, role_name,skill_name):
        self.role_name = role_name
        self.skill_name = skill_name
        

        