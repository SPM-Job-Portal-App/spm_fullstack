from flask import Flask
from role_listings.listingController import listing_bp
from role_application.applicationController import application_bp
from access_control.accessController import access_bp
from staff.staffController import staff_bp
from role.roleContoller import role_bp
from role_skill.roleSkillController import role_skill_bp
from skill.skillController import skill_bp
from staff_skill.staffSkillController import staff_skill_bp;
from models.model import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def drop_tables():
    with app.app_context():
        db.drop_all()

def initialize_databases():
    with app.app_context():
        db.create_all()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://user:password@localhost:3306/db'
db.init_app(app)
initialize_databases()
app.register_blueprint(listing_bp, url_prefix='/listing')
app.register_blueprint(application_bp, url_prefix='/application')
app.register_blueprint(staff_bp, url_prefix='/staff')
app.register_blueprint(role_bp, url_prefix='/role')
app.register_blueprint(staff_skill_bp, url_prefix='/staffskill')
app.register_blueprint(skill_bp, url_prefix='/skill')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
