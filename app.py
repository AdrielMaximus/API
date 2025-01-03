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
@app.route('/meals', methods=['GET'])
def all_meals():
    return jsonify(meals)

#localhost/meal/id (one single meal)
@app.route('/meals/<int:id>', methods=['GET'])
def single_meals(id):
    for meal in meals:
        if meal.get('id') == id:
            return jsonify(meal)

#localhost/meal/id (change a meal)
@app.route('/meals/<int:id>', methods=['PUT'])
def change_meals(id):
    changed_meal=request.get_json()
    for index, meal in enumerate(meals):
        if meal.get('id') == id:
            meals[index].update(changed_meal)
            return jsonify(meals[index])
#localhost/meal/id (delete a meal)
@app.route('/meals/<int:id>', methods=['DELETE'])
def delete_meal(id):
    for index, meal in enumerate(meals):
        if meal.get('id') == id:
            del meals[index]
    return jsonify(meals)

app.run(port=5000, host='localhost', debug=True)