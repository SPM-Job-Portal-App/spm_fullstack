from flask import Flask
from role_listings.role_listing import listing_bp
from role_application.applicationController import application_bp
from role.role_service import role_bp
from models import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://user:password@localhost:3306/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(listing_bp, url_prefix='/listing')
app.register_blueprint(application_bp, url_prefix='/application')
app.register_blueprint(role_bp, url_prefix='/role')

@app.route('/', methods=["GET"])
def test():
    return "Flask API works!"

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)