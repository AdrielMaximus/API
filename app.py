#CRUD
from flask import Flask, jsonify, request

app = Flask(__name__)

meals = [
    {
        'id': 1,
        'name': 'whopper with fries and a shake',
        'franchise': 'Burger King'
    },
    {
        'id': 2,
        'name': 'Mcchiken with extra ketchup',
        'franchise': 'Mcdonalds'
    },
    {
        'id': 3,
        'name': '20 chicken tenders',
        'franchise': 'KFC'
    }
]


#localhost/meals (all meals)
@app.route('/meals')
def all_books():
    return jsonify(meals)

#localhost/meal/id (one single meal)
#localhost/meal/id (change a meal)
#localhost/meal/id (delete a meal)
#Create (Post)
#Read (GET)
#Update (PUT/FETCH)
#DELETE (DELETE)

app.run(port=5000, host='localhost', debug=True)