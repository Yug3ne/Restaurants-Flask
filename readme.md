# Pizza-Restaurants_Flask_CodeChallenge
The Flask Pizza Restaurant API is an API built with Flask to manage pizza restaurant data.

# Features
1. View a list of all restaurants and pizzas.
2. View details of a specific restaurant and the pizzas available there.
3. Create associations between restaurants and pizzas with pricing.
4. Add new restaurants and pizzas to the system.
5. Delete existing restaurants.

# Tools used
1. Flask-sqlalchemy
2. Postman

# Setup
1. Clone the repository to your local machine
2. Activate the virtual environment using the following command ` source venv/bin/activate `
3. Install the the necessary libraries in the requirements.txt file using ` pip install rquirements.txt ` 
4. Move to the server directory and run ` seed.py ` to create new database records to start working with the api
5. Run the FLask api on ` localhost:5555 ` by running ` python app.py `

# Usage/ API Endpoints
1. ### GET /api/v1/restaurants
 Return Json data in the format below: 
 ```json
 [
    {
        "address": "8248 Sean Expressway Apt. 091\nCharlestown, FM 77592",
        "id": 1,
        "name": "Pizza Palace"
    },
    {
        "address": "56853 Barrett Track Suite 778\nStephanieview, CT 72316",
        "id": 2,
        "name": "Mexican Pizza Place"
    },
    {
        "address": "2345 Samantha Mission\nPort Nicole, AK 96246",
        "id": 3,
        "name": "Italian Joint"
    }
]

```
2. ### GET /api/v1/restaurants/:id
If the restaurant exits return Json data in the format below:
```json
{
    "address": "8248 Sean Expressway Apt. 091\nCharlestown, FM 77592",
    "id": 1,
    "name": "Pizza Palace",
    "pizzas": [
        {
            "id": 1,
            "ingredients": "Pizza dough, elote-style corn, cotija cheese, chili powder, lime, cilantro",
            "name": "Mexican Street Corn Pizza"
        },
        {
            "id": 3,
            "ingredients": "Pizza dough, alfredo sauce, garlic chicken, spinach, sun-dried tomatoes, parmesan cheese",
            "name": "Garlic Chicken Alfredo"
        }
    ]
}

```
If the Restaurant do not exist, return the following Json data
```json
{
    "error": "Restaurant not found"
}
```
3. ### DELETE /api/v1/restaurants/:id
If the retaurant exists it should be remoed from the database along with any RestaurantPizza assocaiated with it.
After deleting it should return an empty response body

If the `Restaurant` does not exist, return the following JSON data, along with
the appropriate HTTP status code:

```json
{
    "error": "Restaurant not found"
}
```
4. ### GET /api/v1/pizzas
Return JSON data in the format below:
```json
[
    {
        "id": 1,
        "ingredients": "Pizza dough, elote-style corn, cotija cheese, chili powder, lime, cilantro",
        "name": "Mexican Street Corn Pizza"
    },
    {
        "id": 2,
        "ingredients": "Pizza dough, tandoori chicken, curry sauce, bell peppers, red onion, cilantro, yogurt drizzle",
        "name": "Tandoori Chicken Delight"
    },
    {
        "id": 3,
        "ingredients": "Pizza dough, alfredo sauce, garlic chicken, spinach, sun-dried tomatoes, parmesan cheese",
        "name": "Garlic Chicken Alfredo"
    }
]
```
5. ### POST /api/v1/restaurant_pizzas
This route should create a new `RestaurantPizza` that is associated with an
existing `Pizza` and `Restaurant`. It should accept an object with the following
properties in the body of the request:

```json
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
```
If the `RestaurantPizza` is created successfully, send back a response with the data
related to the `Pizza`:

```json
{
    "id": 1,
    "ingredients": "Pizza dough, elote-style corn, cotija cheese, chili powder, lime, cilantro",
    "name": "Mexican Street Corn Pizza"
}
```

If the `RestaurantPizza` is **not** created successfully, return the following
JSON data, along with the appropriate HTTP status code:

```json
{
  "errors": ["validation errors"]
}
```