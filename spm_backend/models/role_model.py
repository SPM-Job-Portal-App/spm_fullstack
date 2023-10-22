from models.model import db

class Role(db.Model):
    __tablename__ = 'role'
    role_name = db.Column(db.String(255), nullable=False,primary_key=True)
    role_description = db.Column(db.Text, nullable=False)

    def __init__(self, role_name, role_description):
        self.role_name = role_name
        self.role_description = role_description
       
    def json(self):
        return {"Role": self.role_name, "Role Description": self.role_description}
    