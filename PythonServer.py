import flask
from flask import request, jsonify
from PythonBackend import getPendingOrders,getFoodItemsOfCertainCategory

app = flask.Flask(__name__)
app.config["DEBUG"] = True




# A route to return all of the available entries in our catalog.
@app.route('/getOrders', methods=['GET'])
def getOrders():
    return getPendingOrders()

@app.route('/getFoodItems', methods=['GET'])
def getFoodItems():
    category = request.args.get('itemCategory', default = 'Meals', type = str)
    return getFoodItemsOfCertainCategory(category)


app.run()
