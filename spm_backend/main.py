from flask import Flask
from role_listings.role_listing import listing_bp
from role_application.applicationController import application_bp
from role.role_service import role_bp
from models import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def drop_tables():
    with app.app_context():
        db.drop_all()

def initialize_databases():
    with app.app_context():
        db.create_all()

# Try connecting to MySQL on localhost first
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://user:password@localhost:3306/db'

# If unable to connect to localhost, fall back to the "mysql" service defined in Docker Compose
try:
    db.init_app(app)
    app.register_blueprint(listing_bp, url_prefix='/listing')
    app.register_blueprint(application_bp, url_prefix='/application')
    app.register_blueprint(role_bp, url_prefix='/role')
except Exception as e:
    print(f"Failed to connect to MySQL on localhost: {e}")
    
    # Try connecting to the "mysql" service defined in Docker Compose
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://user:password@mysql:3306/db'
    db.init_app(app)
    app.register_blueprint(listing_bp, url_prefix='/listing')
    app.register_blueprint(application_bp, url_prefix='/application')
    app.register_blueprint(role_bp, url_prefix='/role')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
