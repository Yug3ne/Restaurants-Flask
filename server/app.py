from flask import Flask, make_response, jsonify, request
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
        
    def delete(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            Restaurant_Pizza.query.filter_by(restaurant_id = id).delete()
            db.session.delete(restaurant)
            db.session.commit()
            return make_response(
                jsonify([]),
                204
            )
        else:
            return make_response(
                jsonify({"error": "Restaurant not found"}),
                404
            )
api.add_resource(RestaurantsId, '/api/v1/restaurants/<int:id>')

class Pizzas(Resource):
    def get(self):
        pizzas = []
        for pizza in Pizza.query.all():
            pizza_dict = {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            }
            pizzas.append(pizza_dict)
        return make_response(
            jsonify(pizzas),
            200
        )
api.add_resource(Pizzas, '/api/v1/pizzas')

class RestaurantPizzas(Resource): 
    def post(self):
        data = request.json
        try:
            restaurant_pizza = Restaurant_Pizza(price=data['price'], pizza_id=data['pizza_id'], restaurant_id=data['restaurant_id'])
            db.session.add(restaurant_pizza)
            db.session.commit()
            pizza = Pizza.query.get(restaurant_pizza.pizza_id)
            return jsonify({'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients})
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({"errors": ["validation errors"]}), 400

api.add_resource(RestaurantPizzas, '/api/v1/restaurant_pizzas')

if __name__ == '__main__':
    app.run(port=5555, debug=True)