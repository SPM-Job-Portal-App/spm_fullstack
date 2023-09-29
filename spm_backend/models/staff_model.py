from model import db

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_first_name = db.Column(db.String(255), nullable=False)
    staff_last_name = db.Column(db.String(255), nullable=False)
    dept = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    role = db.Column(db.String(255), nullable=False)

    def __init__(self, staff_first_name, staff_last_name, dept, country, email, role):
        self.staff_first_name = staff_first_name
        self.staff_last_name = staff_last_name
        self.dept = dept
        self.country = country
        self.email = email
        self.role = role