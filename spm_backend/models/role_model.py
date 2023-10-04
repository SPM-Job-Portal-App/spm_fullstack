from models.model import db

class Role(db.Model):
    role_name = db.Column(db.String(50), primary_key=True)
    role_desc = db.Column(db.String(255), nullable=False)

    def __init__(self, role_name, role_desc):
        self.role_name = role_name
        self.role_desc = role_desc

