from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)

try:
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        database='user'
    )

    if connection.is_connected():
        print("MySQL connection is successful.")
    else:
        print("MySQL connection is not established.")

except mysql.connector.Error as e:
    print(f"Error: {e}")
finally:
    if 'connection' in locals():
        connection.close()

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/user'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/', methods=["GET"])
def test():
    return "Flask API works!"

@app.route('/users', methods=['GET'])
def getUsers():
    users = User.query.all()
    print(users)
    user_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify(user_list)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)