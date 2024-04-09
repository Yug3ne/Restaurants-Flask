from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates



db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    address = db.Column(db.String)

    restaurant_pizzas = db.relationship('Restaurant_Pizza', backref='restaurant')

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)

    restaurant_pizzas = db.relationship('Restaurant_Pizza', backref='pizza')


class Restaurant_Pizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id=  db.Column(db.Integer, primary_key=True)
    price= db.Column(db.Float, nullable=False)
    pizza_id= db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id= db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)



    @validates
    def validate_price(self, price):
        if not (1 <= price <= 30):
            raise ValueError("Price must be between 1 and 30")
        return price 