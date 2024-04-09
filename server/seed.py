from models import db, Restaurant, Pizza, Restaurant_Pizza
from app import app
from faker import Faker

fake= Faker()

def seeding():
    with app.app_context():
        Pizza.query.delete()
        Restaurant_Pizza.query.delete()
        Restaurant.query.delete()


        # seeding pizza data
        mexican = Pizza(name = "Mexican Street Corn Pizza", ingredients = "Pizza dough, elote-style corn, cotija cheese, chili powder, lime, cilantro")
        tandori = Pizza(name = "Tandoori Chicken Delight", ingredients = "Pizza dough, tandoori chicken, curry sauce, bell peppers, red onion, cilantro, yogurt drizzle")
        garlic = Pizza(name = "Garlic Chicken Alfredo", ingredients = "Pizza dough, alfredo sauce, garlic chicken, spinach, sun-dried tomatoes, parmesan cheese")
        # add pizza to database session
        db.session.add(mexican)
        db.session.add(tandori)
        db.session.add(garlic)
        db.session.commit()
        
        # sedding restaurants data
        rest1 = Restaurant(name = "Pizza Palace", address = fake.address())
        rest2 = Restaurant(name = "Mexican Pizza Place", address = fake.address())
        rest3 = Restaurant(name = "Italian Joint", address = fake.address())
        

        # add restaurant to session
        db.session.add(rest1)
        db.session.add(rest2)
        db.session.add(rest3)
        
        db.session.commit()

        # add restaurant_pizzas
        restaurant_pizza1 = Restaurant_Pizza(restaurant=rest1, pizza=mexican, price=10.99)
        restaurant_pizza2 = Restaurant_Pizza(restaurant=rest1, pizza=garlic, price=12.99)
        restaurant_pizza3 = Restaurant_Pizza(restaurant=rest2, pizza=tandori, price=11.99)

        db.session.add(restaurant_pizza1)
        db.session.add(restaurant_pizza2)
        db.session.add(restaurant_pizza3)
        
        
        db.session.commit()


if __name__ == "__main__":
    print("Sedding Data...")
    seeding()
    print('sedding completed')