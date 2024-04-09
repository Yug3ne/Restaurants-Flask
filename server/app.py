from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Resource, Api

from models import db, Restaurant, Pizza, Restaurant_Pizza

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


# views 
class Index(Resource):
    def get(self):
        response_dict = {
            "home": "Welcome to Pizza/Restaurants API"
        }
        response = make_response(
            jsonify(response_dict),
            200
        )
        return response
    
api.add_resource(Index, '/api/v1/')

# Get restaurants route
class Restaurants(Resource):
    def get(self):
        restaurants = []
        for restaurant in Restaurant.query.all():
            rest_dict = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
            restaurants.append(rest_dict)
        return make_response(
            jsonify(restaurants),
            200
        )
api.add_resource(Restaurants, '/api/v1/restaurants')

class RestaurantsId(Resource):
    def get(self, id):
        restaurant = Restaurant.query.filter_by(id = id).first()

        if restaurant:
            restaurant_pizzas = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
                "pizzas": []
            }
            for restaurant_pizza in restaurant.restaurant_pizzas:
                pizza_dict = {
                    "id": restaurant_pizza.pizza.id,
                    "name": restaurant_pizza.pizza.name,
                    "ingredients": restaurant_pizza.pizza.ingredients
                }
                restaurant_pizzas["pizzas"].append(pizza_dict)
            return make_response(
                jsonify(restaurant_pizzas),
                200
            )
        else:
            return make_response(
                jsonify({"error": "Restaurant not found"}),
                404
            )
api.add_resource(RestaurantsId, '/api/v1/restaurants/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)