from flask import Flask
from role_listings.role_listing_controller import listing_bp
from role_application.role_application import application_bp
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://user:password@localhost:3306/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(listing_bp, url_prefix='/listing')
app.register_blueprint(application_bp, url_prefix='/application')

@app.route('/', methods=["GET"])
def test():
    return "Flask API works!"

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)