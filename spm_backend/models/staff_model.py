from models.model import db

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_first_name = db.Column(db.String(255), nullable=False)
    staff_last_name = db.Column(db.String(255), nullable=False)
    dept = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)

    # Define a foreign key relationship to AccessControl
    role = db.Column(db.Integer, db.ForeignKey('access_control.access_id'), nullable=False)

    # Define a relationship with the AccessControl model
    access_control = db.relationship('AccessControl', backref='staff', foreign_keys=[role])
    skills = db.relationship("StaffSkill", back_populates="staff")


    def __init__(self, id,staff_first_name, staff_last_name, dept, country, email, role):
        self.id =id
        self.staff_first_name = staff_first_name
        self.staff_last_name = staff_last_name
        self.dept = dept
        self.country = country
        self.email = email
        self.role = role

    def json(self):
        return {"Staff Name": self.staff_first_name + " " + self.staff_last_name, "Department": self.dept, "Country": self.country, "Email": self.email, "Role": self.role}
    
