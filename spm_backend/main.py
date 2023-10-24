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

# import Cronjob class from cronjob.py and start cron job
def start_cronjob():
    cronjob_module = importlib.import_module("open_close_listing_cronjob.cronjob")
    cronjob_class = getattr(cronjob_module, "Cronjob")
    cronjob_class.open_close_role_listing_cronjob()

# import TestCronjob class from test_cronjob.py and start cron job
# cronjob for test
def start_test_cronjob():
    cronjob_module = importlib.import_module("open_close_listing_cronjob.test_cronjob")
    cronjob_class = getattr(cronjob_module, "TestCronjob")
    cronjob_class.open_close_role_listing_cronjob()

@app.route('/')
def test():
    return "test"

app.config['SQLALCHEMY_DATABASE_URI'] = ''


db.init_app(app)
initialize_databases()
app.register_blueprint(listing_bp, url_prefix='/listing')
app.register_blueprint(application_bp, url_prefix='/application')
app.register_blueprint(staff_bp, url_prefix='/staff')
app.register_blueprint(role_bp, url_prefix='/role')
app.register_blueprint(staff_skill_bp, url_prefix='/staffskill')
app.register_blueprint(skill_bp, url_prefix='/skill')
app.register_blueprint(role_skill_bp, url_prefix='/roleskill')
app.register_blueprint(access_bp, url_prefix='/access')

# Create a thread for the timer
cronjob_thread = threading.Thread(target=start_cronjob)

if __name__ == '__main__':
    # Uncomment to run cronjob to open or close role listings
    # cronjob_thread.start()

    # debug = True does not work well with multithreading because once you save some code and the Flask server restarts, there will be some error. So I commented out the "cronjob_thread.start()" line. If you want to use it, set change debug to False and uncomment the line
    app.run(host='0.0.0.0', port=5000, debug=True)

