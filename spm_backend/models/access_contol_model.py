from models.model import db

class AccessControl(db.Model):
    __table_name__ = 'access_control'
    access_id = db.Column(db.Integer, primary_key=True)
    access_control_name = db.Column(db.String(20), nullable=False)

  

    def __init__(self,access_id, access_control_name):
        self.access_id = access_id
        self.access_control_name = access_control_name

    def json(self):
        return {"Access Id": self.access_id, "Access Control Name": self.access_control_name}
    


