from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Restaurant, Pizza, Restaurant_Pizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


# views 
@app.route('/')
def index():
    response_dict = {
            "home": "Welcome to Pizza/Restaurants API"
        }
    response = make_response(
        jsonify(response_dict),
            200
        )
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)