from flask import Flask
from role_listings.listingController import listing_bp
from role_application.applicationController import application_bp
from staff.staffController import staff_bp
from role.roleContoller import role_bp
from role_skill.roleSkillController import role_skill_bp
from skill.skillController import skill_bp
from models.model import db
from flask_cors import CORS
import importlib
import threading

app = Flask(__name__)
CORS(app)

def drop_tables():
    with app.app_context():
        db.drop_all()

def initialize_databases():
    with app.app_context():
        db.create_all()

# import Timer class from timer.py and start cron job
def start_timer():
    timer_module = importlib.import_module("timer.timer")
    timer_class = getattr(timer_module, "Timer")
    timer_class.open_role_listing_job()

# import Timer class from timer.py and start cron job
# timer for test
def start_test_timer():
    timer_module = importlib.import_module("timer.test_timer")
    timer_class = getattr(timer_module, "TestTimer")
    timer_class.open_role_listing_job()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://user:password@localhost:3306/db'
db.init_app(app)
initialize_databases()
app.register_blueprint(listing_bp, url_prefix='/listing')
app.register_blueprint(application_bp, url_prefix='/application')
app.register_blueprint(staff_bp, url_prefix='/staff')
app.register_blueprint(role_bp, url_prefix='/role')
app.register_blueprint(role_skill_bp, url_prefix='/roleskill')
app.register_blueprint(skill_bp, url_prefix='/skill')
# app.register_blueprint(role_bp, url_prefix='/role')

# Create a thread for the timer
timer_thread = threading.Thread(target=start_timer)

if __name__ == '__main__':
    timer_thread.start()
    app.run(host='localhost', port=5000, debug=False)
